#!/usr/bin/python3

"""prints titles of first 10 hot posts listed for a given subreddit"""


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": 'CodeZero'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for i in data['data']['children']:
            print(i['data']['title'])
    else:
        print(None)


