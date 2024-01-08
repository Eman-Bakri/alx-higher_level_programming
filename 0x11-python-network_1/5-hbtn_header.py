#!/usr/bin/python3
"""
Shows the X-Request-Id variable value
"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    headers = r.headers.get('X-Request-Id')
    print(headers)
