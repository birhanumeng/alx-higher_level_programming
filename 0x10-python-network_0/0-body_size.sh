#!/bin/bash
# sends a request to argument URL, and displays the size of the body of the response
curl -s "$1" | wc -c
