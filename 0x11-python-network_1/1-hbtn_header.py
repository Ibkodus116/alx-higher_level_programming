#!/usr/bin/python3
"""A Python script that takes in a URL, sends a
request to the URL and displays the value of the
X-Request-Id variable found in the header of the
response.
"""

import urllib.request as lib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with lib.urlopen(url) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
