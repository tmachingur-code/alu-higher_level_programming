#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""

import requests
import sys


if __name__ == "__main__":
    data = {"email": sys.argv[2]}

    response = requests.post(sys.argv[1], data=data)

    print(response.text)
