#!/usr/bin/python3
"""
Prints github id by using credintals
"""
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    import requests
    import sys
    user = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        print(response.json().get('id'))
    except ValueError:
        print('None')
