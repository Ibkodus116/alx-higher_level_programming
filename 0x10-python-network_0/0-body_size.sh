#!/usr/bin/env bash

# Check if the script was called with a URL
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and store the response body in a variable
# response=$(curl -sI $1 | grep -i content-length | awk '{print $2}' | tr -d '\r')
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
# Display the size of the response body
#echo "this is $response"
