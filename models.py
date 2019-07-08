from google.appengine.ext import ndb

"""[Model for User Profiles]
"""
class UserProfile(ndb.Model):
	
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	username = ndb.StringProperty()
	email = ndb.StringProperty()
	user_id = ndb.StringProperty()
	profile_pic = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

	"""[Creates the User]
	Returns:
		[Key] -- [Key of New Entry in UserProfile Table]
	"""
	@classmethod
	def create_user(cls, email, user_id):
		user = cls(email = email, user_id = user_id)
		return user.put()

	"""[Checks if User Exists in the UserProfile Table]
	Returns:
		[Boolean] -- [True if User Exists else False]
	"""
	@classmethod
	def is_user_exist(cls, email):
		check_user = cls.query(cls.email == email).get()
		if check_user:
			return True
		return False

"""[Model for Communication among Users]
"""
class Chats(ndb.Model):
	
	sender_key = ndb.KeyProperty(kind=UserProfile)
	receiver_key = ndb.KeyProperty(kind=UserProfile)
	content = ndb.TextProperty()
	sent_time = ndb.DateTimeProperty(auto_now_add=True)
