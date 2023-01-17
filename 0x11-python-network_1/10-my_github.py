#!/usr/bin/python3
"""takes your GitHub credentials (username and password)"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    print(req.json().get('id'))
