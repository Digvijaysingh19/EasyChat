def post_info(self):
    data = UserProfile.query().fetch()
    row = []
    for d in data:
        row.append({
            'first_name': d.first_name,
            'last_name' : d.last_name,
            'key' : d.key.urlsafe(),
        })
    json_dict = json.dumps(row)
    self.response.write({"data" : json_dict})

    