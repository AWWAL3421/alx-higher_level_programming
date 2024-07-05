#!/bin/bash

# This script takes in a URL, sends a GET request to the URL, and displays the body of the response

# Take in the URL as argument
url="$1"

# Send GET request and store response body in a variable
response=$(curl -s -w "\n%{http_code}" "$url")

# Get status code from response
status_code=$(echo "$response" | tail -n1)

# If status code is 200, display response body
if [[ "$status_code" == "200" ]]; then
  body=$(echo "$response" | head -n -1)
  echo "$body"
else
  echo "Error: Response status code is not 200"
fi
