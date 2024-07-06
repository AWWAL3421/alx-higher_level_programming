#!/bin/bash
# This script sends a request to a URL and shows the size in bytes.
curl -s "$1" | wc -c
