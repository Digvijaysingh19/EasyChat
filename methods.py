from models import *
import json

def post_info():
    data = UserProfile.query().fetch()
    row = []
    for d in data:
        row.append({
            'first_name': d.first_name,
            'last_name' : d.last_name,
            'key' : d.key.urlsafe(),
            'email' : d.email
        })
    self.response.write(json.dumps(row))

def post_data(user_email, user_id):
    user = UserProfile()
    user.email = user_email
    user.user_id = user_id 
    user.put()

def post_current_user(user_email):
    user1_key = UserProfile.query(UserProfile.email == user_email).fetch(keys_only=True)
    print(user1_key[0].urlsafe())
    return user1_key[0].urlsafe()