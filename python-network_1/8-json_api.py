#!/usr/bin/python3
"""Sends a POST request and displays information from a JSON response."""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()

        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
