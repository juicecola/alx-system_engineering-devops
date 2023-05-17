import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        None
    """

    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "MyRedditClient"}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            for post in data["data"]["children"]:
                title = post["data"]["title"]
                print(title)
        else:
            print("None")
    except requests.RequestException as e:
        print("None")

# Example usage
top_ten("programming")

