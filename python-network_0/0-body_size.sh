#!/bin/bash
# takes URL and displays the size of the response body
curl -s "$1" | wc -c
