#!/usr/bin/python3

"""number of subcribers for a given subreddit."""

import requests
import sys


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'Codezero'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    print("{:d}").fortmat(number_of_subscribers(subreddit))
