from google.appengine.datastore.datastore_query import Cursor
import time
from models import *
import webapp2
import json
from methods import *
from google.appengine.api import users
import datetime
import secret
from onesignal import OneSignal, DeviceNotification

"""[The CurrentUser class sends the currently logged user info in the response]
"""
class CurrentUser(webapp2.RequestHandler):
    def get(self):
        add_user()
        time.sleep(1)
        current_user = get_user()
        user1_key = current_user_key()
        current_user_info = {
            "user1_key" : user1_key.urlsafe(),
            "user1_email" : current_user.email()
        }
        self.response.write(json.dumps(current_user_info))

"""[The Profile class User Profile Detail Edits ]
"""						
class Profile(webapp2.RequestHandler):
	def post(self):
		req = json.loads(self.request.body)
		user = UserProfile()
		user.populate(
			first_name = req.get('firstname'),
			last_name = req.get('lastname'),
			username = req.get('username'),
			profile_pic = req.get('dp'))

		user.put()
		self.response.write({"Message" : "SignUp Successful."})
		time.sleep(1)
		post_info(self)

"""[The Index class handles the sending of all Users Data to Front-end]
"""
class Index(webapp2.RequestHandler):
    def get(self):
        add_user()
        json_dict = send_info()
        self.response.write(json_dict)

"""[The MainPage class handles all the operations happening on the main page of the app]
"""					
class MainPage(webapp2.RequestHandler):
    def post(self):
        add_user()
        time.sleep(1)
        req = json.loads(self.request.body)
        key1 = current_user_key()
        key2 = ndb.Key(urlsafe=req.get('user2_key'))

        # chats, _cursor, more = Chats.query(Chats.sender_key.IN([key1,key2]) , Chats.receiver_key.IN([key1,key2])).\
        #                        order(Chats.key).fetch_page(15, start_cursor=cursor)
        limit = 15
        if self.request.get('offset'):
            offset = self.request.get('offset') + limit
        else:
            offset = 0
        chats = Chats.query(Chats.sender_key.IN([key1,key2]) , Chats.receiver_key.IN([key1,key2])).\
                               order(-Chats.sent_time).fetch(limit,offset = offset)

        badges = Chats.query(Chats.receiver_key == key1, Chats.sender_key == key2).fetch()

        for b in badges:
            b.unread = False
            b.put()
        #Sends last 10 chats between user1 and user2
        row = []
        for data in chats:
            row.append(
                {
                    'chat_key' : data.key.urlsafe(),
                    'user1_key' : data.sender_key.urlsafe(),
                    'user2_key' : data.receiver_key.urlsafe(),
                    'content' : data.content,
                    'chat_time' : data.sent_time.strftime("%X")
                }
            )

        self.response.write(json.dumps({"offset":offset,"data":json.dumps(row)}))

"""[The Message class sends the chat messages into the database]
"""
class Message(webapp2.RequestHandler):
    def post(self):
        add_user()
        time.sleep(1)
        req = json.loads(self.request.body)
        chat = Chats()
        key1 = current_user_key()
        key2 = ndb.Key(urlsafe=req.get('user2_key'))
        chat.populate(
            sender_key = key1,
            receiver_key = key2,
            content = req.get('content'))
        chat.put()

        user = get_user()
        client = OneSignal(secret.onesignal_app_id, secret.onesignal_rest_api_key)
        notification_to_users = DeviceNotification(
            contents={
                "en": req.get('content')
            },
            headings={
                "en": user.email()
            },
            # include_player_ids=["b6fc8584-4010-47ad-8620-3150ecdcf9c7"]
            include_external_user_ids=[req.get('user2_key')]
        )
        client.send(notification_to_users)

app = webapp2.WSGIApplication([
  ('/handlers/current_user', CurrentUser),
  ('/handlers/edit', Profile),
  ('/handlers/chat', Index),
  ('/handlers/mainpage', MainPage),
  ('/handlers/msgsent', Message)
], debug=True)