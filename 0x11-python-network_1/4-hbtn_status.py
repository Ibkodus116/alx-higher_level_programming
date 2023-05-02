#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    http = requests.get(url)

    print('Body response:')
    print(f'\t- type: {type(http.text)}')
    print(f'\t- content: {http.text}')
