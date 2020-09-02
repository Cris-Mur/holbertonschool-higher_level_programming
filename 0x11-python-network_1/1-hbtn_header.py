#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
from urllib import request
if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.getheader('X-Request-Id'))
