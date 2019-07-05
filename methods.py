from models import *
import json
from google.appengine.api import users
import time

"""[Sends all Existing Users Data to the Front-end]
Returns:
    [String] -- [Array of User Info]
"""
def send_info():
    current_user = get_user()
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

"""[Sends the Currently Logged User's Key ]
Returns:
    [Key] -- [Key of Current User]
"""
def current_user_key():
    current_user = get_user()
    user1_key = UserProfile.query(UserProfile.email == current_user.email()).get(keys_only=True)
    if user1_key:
        return user1_key

"""[Adds New User]
"""
def add_user():
    user = UserProfile()
    current_user = get_user()
    if not user.is_user_exist(current_user.email()):
        user.create_user(current_user.email(), current_user.user_id())

"""[Gets Current User Info]
Returns:
    [User] -- [Current User]
"""
def get_user():
    return users.get_current_user()