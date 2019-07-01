from models import *
import json

def post_info(self):
    data = UserProfile.query(UserProfile.email != self.email()).fetch()
    row = []
    for d in data:
        row.append({
            'first_name': d.first_name,
            'last_name' : d.last_name,
            'key' : d.key.urlsafe(),
            'email' : d.email
        })
    self.response.write(json.dumps(row))

def post_data(self):
    user = UserProfile()
    user.email = self.email()
    user.user_id = self.user_id() 
    user.put()

def post_current_user(self):
    user1_key = UserProfile.query(UserProfile.email == self.email()).fetch(keys_only=True)
    print(user1_key[0].urlsafe())
    return user1_key[0].urlsafe()