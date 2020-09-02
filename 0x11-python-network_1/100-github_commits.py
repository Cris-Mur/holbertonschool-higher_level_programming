#!/usr/bin/python3
""" display github commits """
from requests import get, auth
import sys
if __name__ == '__main__':
    try:
        repo = sys.argv[1]
        user = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
        request = get(url)
        jsonify = request.json()
        for i in range(0, 10):
            print('{}: {}'.format(jsonify[i].get('sha'), jsonify[i].get(
                'commit').get('author').get('name')))
    except:
        pass
