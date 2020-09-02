#!/usr/bin/python3
""" Python script that takes in a URL and an email """
from urllib import request, parse
import sys
if __name__ == '__main__':
    email = parse.urlencode({'email': sys.argv[2]})
    email = email.encode('ascii')
    re = request.Request(sys.argv[1], email)
    with request.urlopen(re) as response:
        body = response.read()
        print(body.decode('utf-8'))
