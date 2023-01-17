#!/usr/bin/python3
"""takes in a URL, sends a request to the URL using request and haddle error"""
import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
