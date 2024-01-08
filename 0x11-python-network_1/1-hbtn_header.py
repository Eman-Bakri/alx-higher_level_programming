#!/usr/bin/python3
"""
Displays X-Request-Id variable value
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
