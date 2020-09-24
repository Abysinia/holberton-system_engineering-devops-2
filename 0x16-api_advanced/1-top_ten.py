#!/usr/bin/python3
""" Prints the titles of the first 10 hot posts listed
for a given subreddit. """

import json
import requests


def top_ten(subreddit):
    """top_ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, allow_redirects=False,
                     headers={'user-agent': 'myUser'})

    if r.status_code == 200:
        data = r.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print('None')
