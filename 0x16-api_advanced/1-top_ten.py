#!/usr/bin/python3

import requests

def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "CodeZero"}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("Error: Unable to retrieve posts from the subreddit")
    except requests.RequestException as e:
        print("Error: An exception occurred during the API request:", e)

# Example usage: python3 1-main.py programming
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
