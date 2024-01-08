#!/usr/bin/python3
"""module to  fetch a specific url"""

if __name__ == "__main__":
    import urllib.request
    requrl = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(requrl) as response:
        response_content = response.read()
        print("Body response:")
        print(f"\t- type: {type(response_content)}")
        print(f"\t- content: {response_content}")
        print(f"\t- utf8 content: {response_content.decode()}")
