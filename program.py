https://redshelf.com/library/



# #!/usr/bin/env python
import requests
import json



class Authorisation:

    auth = ('admin', 'admin')

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def authorisation_id(self):
        pass

class User(Authorisation):



    def __init__(self, uri, name, password):

        self.uri = uri
        self.name = name
        self.password = password

    def get_users(self):
        # Gets all users

        r = requests.get('http://{}'.format(self.uri), auth=self.auth)
        string_of_users = r.json()
        for element in string_of_users:

            return "ID: {} \t NAME: {}".format(element['id'], element['name'])

    def post_users(self):
        # Adds new user

        payload = {'name': self.name, 'password': self.password}
        r = requests.post('http://{}'.format(self.uri), json=payload)

        return r.status_code

    def get_user_id(self):
        # Gets users ID after typing it's name

        list_of_code = []
        r = requests.get('http://{}'.format(self.uri), auth=self.auth)
        string_of_users = r.json()
        for element in string_of_users:
            list_of_code.append(element['name'])
            if self.name in list_of_code:
                User.user_id = element['id']
        return User.user_id

    def put_user_id(self):
        # Modifies users password

        payload = {'name': self.name, 'password': self.password}
        r = requests.put('http://{}/{}'.format(self.uri, User.user_id), auth=self.auth, data=json.dumps(payload))

        return r.status_code

    def delete_user(self):
        # Extinguishes user for ever and ever!!!

        payload = {'name': self.name, 'password': self.password}
        r = requests.delete('http://{}/{}'.format(self.uri, User.user_id), auth=self.auth, data=json.dumps(payload))

        return r.status_code




