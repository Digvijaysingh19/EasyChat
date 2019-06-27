from models import *
import json

def post_info(self):
    data = UserProfile.query().fetch()
    row = []
    for d in data:
        row.append({
            'first_name': d.first_name,
            'last_name' : d.last_name,
            'key' : d.key.urlsafe(),
            'username' : d.username
        })
    self.response.write(json.dumps(row))