#!/usr/bin/python3
"""
send a POST request to the passed URL with email
"""


if __name__ == "__main__":
    import requests
    import sys
    vals = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=vals)
    print(r.text)
