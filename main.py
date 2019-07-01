from google.appengine.datastore.datastore_query import Cursor
import time
from models import *
import webapp2
import json
from methods import *
from google.appengine.api import users

current_user = users.get_current_user()


"""[The SignUp class handles the new account creations and redirects to the
	main page after successful account creation]
"""						
class SignUp(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)
		user = UserProfile()
		user.populate(
			first_name = req.get('firstname'),
			last_name = req.get('lastname'),
			username = req.get('username'),
			email = current_user.email(),
			user_id = current_user.user_id(),
			profile_pic = req.get('dp'))

		user.put()
		self.response.write({"Message" : "SignUp Successful."})
		time.sleep(1)
		post_info(self)

"""[The MainPage class handles all the operations happening on the main page of the app]
"""					
class MainPage(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)

		key1 = post_current_user(current_user.email())
		key2 = ndb.Key(urlsafe=req.get('user2_key'))
		
		#Checks if there is a cursor in the request
		if self.request.get('cursor'):	
			cursor = Cursor(urlsafe=self.request.get('cursor'))
		else:
			cursor = None
		
		chats, _cursor, more = Chats.query(ndb.AND(ndb.OR(Chats.sender_key == key1,Chats.sender_key == key2),\
							   ndb.OR(Chats.receiver_key == key2,(Chats.receiver_key == key1)))).\
							   order(-Chats.sent_time).fetch_page(10, start_cursor=cursor)
		
		#Sends last 10 chats between user1 and user2
		row = []
		for data in chats:
			row.append(
				{
					'chat_key' : data.key.urlsafe(),
					'user1_key' : data.sender_key.urlsafe(),
					'user2_key' : data.receiver_key.urlsafe(),
					'content' : data.content,
					'chat_time' : str(data.sent_time) 
				}
			)
		
		self.response.write({more,json.dumps(row),_cursor.urlsafe()})

"""[The Message class sends the chat messages into the database]
"""
class Message(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)
		chat = Chats()
		key1 = post_current_user(current_user.email())
		key2 = ndb.Key(urlsafe=req.get('user2_key'))
		chat.populate(
			sender_key = key1,
			receiver_key = key2,
			content = req.get('content'))
		chat.put()

class Index(webapp2.RequestHandler):
	def get(self):
		json_dict = post_info(current_user)
		self.response.write(json_dict)
		print(json_dict)

class Main(webapp2.RequestHandler):
	def get(self):
		print(current_user)
		user_email = current_user.email()
		check_user = UserProfile.query(UserProfile.email == user_email).get()
		if not check_user:
			post_data(user_email,current_user.user_id())
		current_user_key = post_current_user(user_email)
		user_key = {
			"user1_key" : current_user_key,
			"user1_email" : user_email
		}
		self.response.write(json.dumps(user_key))
		self.redirect("/chat#!/chat")
		
app = webapp2.WSGIApplication([
   webapp2.Route('/', Main),
  ('/handlers/signup', SignUp),
  ('/handlers/msgsent', Message),
  ('/handlers/mainpage', MainPage),
  ('/handlers/chat', Index)
], debug=True)