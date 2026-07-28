#!/usr/bin/python3
"""Uses GitHub API authentication to retrieve a user's GitHub ID."""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )

    data = response.json()

    print(data.get("id"))
