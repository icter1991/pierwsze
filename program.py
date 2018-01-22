# #!/usr/bin/env python
import requests
import json


auth = ('admin', 'admin')


def authorisation_id():
    pass


def get_users(host_id):
    # Gets all users

    r = requests.get('http://{}'.format(host_id), auth=auth)
    string_of_users = r.json()
    for element in string_of_users:

        return "ID: {} \t NAME: {}".format(element['id'], element['name'])

def post_users(host_id, name, password):
    # Adds new user

    payload = {'name': name, 'password': password}
    r = requests.post('http://{}'.format(host_id), json=payload)

    return r.status_code == 200

def get_user_id(host_id, name):
    # Gets users ID after typing it's name

    list_of_code = []
    r = requests.get('http://{}'.format(host_id), auth=auth)
    string_of_users = r.json()
    for element in string_of_users:
        list_of_code.append(element['name'])
        if name in list_of_code:

            return element['id']

def put_user_id(host_id, user_id, name, password):
    # Modifies users password

    payload = {'name': name, 'password': password}
    r = requests.put('http://{}/{}'.format(host_id, user_id), auth=auth, data=json.dumps(payload))

    return r.status_code == 200

def delete_user(host_id, user_id, name, password):
    # Extinguishes user for ever and ever!!!

    payload = {'name': name, 'password': password}
    r = requests.delete('http://{}/{}'.format(host_id, user_id), auth=auth, data=json.dumps(payload))

    return r.status_code == 200



