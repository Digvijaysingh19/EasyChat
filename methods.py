from models import *
import json

def post_info(current_user):
    data = UserProfile.query(UserProfile.email != current_user.email()).fetch()
    row = []
    for d in data:
        row.append({
            'first_name': d.first_name,
            'last_name' : d.last_name,
            'key' : d.key.urlsafe(),
            'email' : d.email
        })
    return json.dumps(row)

def post_data(user_email,user_id):
    user = UserProfile()
    user.email = user_email
    user.user_id = user_id 
    user.put()

def post_current_user(user_email):
    user1_key = UserProfile.query(UserProfile.email == user_email).get(keys_only=True)
    if user1_key:
        print (user1_key.urlsafe())
        return user1_key.urlsafe()