from google.appengine.ext import ndb

class UserProfile(ndb.Model):
	"""Model for User Profiles"""
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

class Chats(ndb.Model):
	"""Model for Communication among Users"""
	sender_key = ndb.KeyProperty(kind=UserProfile)
	receiver_key = ndb.KeyProperty(kind=UserProfile)
	content = ndb.TextProperty()
	sent_time = ndb.DateTimeProperty(auto_now_add=True)
