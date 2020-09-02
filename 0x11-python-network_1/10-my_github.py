#!/usr/bin/python3
""" Python script that takes your Github credentials (username & password) """
from requests import get, auth
import sys
if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pw = sys.argv[2]
    pet = get(url, auth=auth.HTTPBasicAuth(user, pw))
    print(pet.json().get('id'))
