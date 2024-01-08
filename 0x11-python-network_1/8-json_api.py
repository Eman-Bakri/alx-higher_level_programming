#!/usr/bin/python3
"""
Post request to search user
"""


if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        output = r.json()
        if bool(output) is False:
            print("No result")
        else:
            print("[{}] {}".format(output['id'], output['name']))
    except ValueError:
        print("Not a valid JSON")
