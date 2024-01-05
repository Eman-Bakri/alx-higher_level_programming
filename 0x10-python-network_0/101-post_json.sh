#!/bin/bash
# JSON POST request.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
