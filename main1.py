from google.appengine.datastore.datastore_query import Cursor
from models import *
import webapp2
import json
from methods import *

"""[The Login class is a Handler that checks for the credentials provided
	by the user and if they match from the database then it redirects to the 
	main page]
"""
class Login(webapp2.RequestHandler):
	def post(self):
		
		req = json.loads(self.request.body)
		
		user = UserProfile()
		user.populate(
			username = req.get('username'),
			password = req.get('password'))
		
		#Checks credentials from database
		user_data = UserProfile.query(UserProfile.username == user.username, UserProfile.password == user.password).get()
		if (user_data):
			self.response.write("Message" : "Login Successful")
			post_info()
		else:
			self.response.write({"Error" : "Incorrect Username or Password !"})

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
			password = req.get('password'))

		#Checks in the database whether the username already exists or not
		check_user = UserProfile.query(UserProfile.username == user.username).get()
		if (check_user):
			self.response.write({"Error" : "Username already exists !"})
		else:
			user.put()
			self.response.write({"Message" : "SignUp Successful."})
			post_info(self)

"""[The MainPage class handles all the operations happening on the main page of the app]
"""					
class MainPage(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)

		key1 = ndb1.Key(urlsafe=req.get('user1_key'))
		key2 = ndb.Key(urlsafe=req.get('user2_key'))
		
		#Checks if there is a cursor in the request
		if self.request.get('cursor'):	
			cursor = Cursor(urlsafe=self.request.get('cursor'))
		else:
			cursor = None
		
		chats, _cursor, more = Chats.query(Chats.sender_key == key1 or key2,\
							   Chats.receiver_key == key1 or key2).\
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
		
		json_dict = json.dumps(row)
		self.response.write({"more" : more, "data" : json_dict, "cur" :  _cursor.urlsafe()})

"""[The Message class sends the chat messages into the database]
"""
class Message(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)
		chat = Chats()
		key1 = ndb.Key(urlsafe=req.get('user1_key'))
		key2 = ndb.Key(urlsafe=req.get('user2_key'))
		chat.populate(
			sender_key = key1,
			receiver_key = key2,
			content = req.get('content'))
		chat.put()

app = webapp2.WSGIApplication([
  ('/', Login),
  ('/signup', SignUp),
  ('/msgsent', Message),
  ('/mainpage', MainPage)
], debug=True)
