#!/usr/bin/python3
import urllib.request as lib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with lib.urlopen(url) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
