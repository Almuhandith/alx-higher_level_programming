#!/usr/bin/python3
"""
Takes your github credentials (username and password) and uses the github API
to display your id
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    response = get(url, auth=(username, password))
    json = response.json()

    print(json.get('id'))
