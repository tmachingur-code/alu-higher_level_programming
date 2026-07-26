#!/bin/bash
# Sends a request that satisfies the catch_me endpoint requirements.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
