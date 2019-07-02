from google.appengine.ext import ndb

class UserProfile(ndb.Model):
	"""Model for User Profiles"""
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	username = ndb.StringProperty()
	email = ndb.StringProperty()
	user_id = ndb.StringProperty()
	profile_pic = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def create_user(cls, email, user_id):
		user = cls(email = email, user_id = user_id)
		return user.put()

	@classmethod
	def is_user_exist(cls, email):
		check_user = cls.query(cls.email == email).get()
		if check_user:
			return True
		return False

class Chats(ndb.Model):
	"""Model for Communication among Users"""
	sender_key = ndb.KeyProperty(kind=UserProfile)
	receiver_key = ndb.KeyProperty(kind=UserProfile)
	content = ndb.TextProperty()
	sent_time = ndb.DateTimeProperty(auto_now_add=True)
