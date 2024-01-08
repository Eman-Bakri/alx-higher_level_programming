#!/usr/bin/python3
"""
used a POST request to pass URL with email as a parameter
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = sys.argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))
