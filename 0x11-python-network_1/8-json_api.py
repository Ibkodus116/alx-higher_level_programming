#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data)

    try:
        json_res = response.json()
        if json_res:
            print(f"[{json_res.get('id')}] {json_res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
