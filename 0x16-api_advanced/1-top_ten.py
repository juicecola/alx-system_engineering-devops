#!/usr/bin/python3

"""this coderetrieve top ten hot topics per subreddit"""
import requests


def top_ten(subreddit):
    """get top ten hot topics"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'Bazeng'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
