#!/usr/bin/python3
""" queries the Reddit API and returns a list
containing the titles of all hot articles for
a given subreddit. If no results are found
for the given subreddit, the function should return None.

 """

import json
import requests


def recurse(subreddit, hot_list=[]):
    """recurse"""

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".
        format(subreddit), allow_redirects=False,
        headers={'User-Agent': 'Something here'})

    if response.ok:
        print('None')
    else:
        print("None")
