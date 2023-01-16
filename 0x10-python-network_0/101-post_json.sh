#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sHd "Content-Type: application/json" "$(cat "$2")" "$1"
