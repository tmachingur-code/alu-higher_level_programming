#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""

from urllib import request, parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
