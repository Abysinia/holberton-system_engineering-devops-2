#!/usr/bin/python3
""" queries the Reddit API and 
prints the titles of the first 10 hot posts listed
 for a given subreddit """

import requests
import json


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit))

    if response.status_code == 200:
        myData = json.loads(response.text)
        return myData["data"]["subscribers"]
    else:
        return 0
