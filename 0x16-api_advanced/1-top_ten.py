#!/usr/bin/python3
""" Prints the titles of the first 10 hot posts listed
for a given subreddit. """

import json
import requests


def top_ten(subreddit):
    """top_ten"""

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".
        format(subreddit), allow_redirects=False,
        headers={'User-Agent': 'Something here'})

    if response.ok:
        myData = json.loads(response.text)
        for post in myData["data"]["children"][:10]:
            print(post.get('data').get('title'))
    else:
        print("None")
