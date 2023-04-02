#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
response=$(curl -sI "$1" | grep -i content-length | awk '{print $2}'| tr -d '\r\n')

#response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

echo "$response"
