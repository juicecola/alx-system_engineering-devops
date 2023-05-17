#!/usr/bin/python3

"""retrieve top ten hot topics per subreddit"""
import requests

def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "CodeZero"}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            for i in data["data"]["title"]:
                print(i["data"]["title"])
        else:
            print("Error: Unable to retrieve posts from the subreddit")
    except requests.RequestException as e:
        print("Error: An exception occured during the API request:", e)
