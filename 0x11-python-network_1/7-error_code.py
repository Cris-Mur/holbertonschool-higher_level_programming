#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
import requests
import sys
if __name__ == '__main__':
    rqt = requests.get(sys.argv[1])
    if rqt.status_code > 400:
        print('Error code:', rqt.status_code)
    else:
        print(rqt.text)
