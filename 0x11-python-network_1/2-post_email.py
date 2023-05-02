#!/usr/bin/pyhon3
"""
A Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as
a parameter, and displays the body of the respons
(decoded in utf-8)
"""

from urllib import parse, request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('ascii')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
