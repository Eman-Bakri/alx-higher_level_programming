#!/bin/bash
# response body size
curl -sI "$1" | awk '/Content-Length/{print $2}'
