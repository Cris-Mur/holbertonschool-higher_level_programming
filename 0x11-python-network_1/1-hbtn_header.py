#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    url = request.Request(argv[1])
    with request.urlopen(url) as res:
        print(res.headers.get('X-Request-Id'))
