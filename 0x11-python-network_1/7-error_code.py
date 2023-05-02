#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request
to the URL and displays the body of the response
'''
import requests
import sys

data = requests.get(sys.argv[1])

if data.status_code >= 400:
    print(f'Error code: {data.status_code}')
else:
    print(data.content.decode('utf-8'))
