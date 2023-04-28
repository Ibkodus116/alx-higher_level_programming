#!/usr/bin/env bash
#send a request to the URL and store the response body in a variable
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
