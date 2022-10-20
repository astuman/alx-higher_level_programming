#!/bin/bash
# it take a URL sends a request to that URL and display the size of the body

curl -sI "$1" | grep 'content-length:' | cut -d' ' -f2
