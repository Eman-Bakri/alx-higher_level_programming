#!/usr/bin/python3
"""
by sending a request to the URL and displays response body
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
