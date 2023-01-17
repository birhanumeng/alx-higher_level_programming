#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge."""
import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)

    for i in range(10):
            print("{}: {}".format(req.json()[i].get("sha"),
                                  req.json()[i].get("commit").
                                  get("author").get("name")))
