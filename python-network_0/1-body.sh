#!/bin/bash
# Sends a GET request and displays the body only for status code 200.
curl -sL -w "%{http_code}" "$1" -o /tmp/body | grep -q 200 && cat /tmp/body
