#!/usr/bin/python3
"""takes in a URL, sends a request to the URL using requests packeges"""
import sys
import requests


if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
