#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sLX PUT -d "user_id=98" -H "You got me!" 0.0.0.0:5000/catch_me
