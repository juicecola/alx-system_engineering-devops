#!/usr/bin/python3

"""recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "CodeZero"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()["data"]
    hot_list += [post["data"]["title"] for post in data["children"]]
    after = data["after"]
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list

