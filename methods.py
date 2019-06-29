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

def post_data(user_email):
    user = UserProfile()
    user.email = user_email
    user.put()
