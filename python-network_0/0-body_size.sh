#!/bin/bash
# Sends a GET request to a URL and displays the size of the response body.
curl -sL "http://$1" | wc -c
