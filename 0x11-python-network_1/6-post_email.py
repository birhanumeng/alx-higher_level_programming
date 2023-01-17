#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request"""
import sys
import requests


if __name__ == "__main__":

    data = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data)
    print(req.text)
