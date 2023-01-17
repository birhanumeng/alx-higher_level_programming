#!/usr/bin/python3
"""takes a URL and an email, sends a POST request to passed URL"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
