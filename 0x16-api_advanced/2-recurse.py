#!/usr/bin/python3
""" queries the Reddit API and returns a list
containing the titles of all hot articles for
a given subreddit. If no results are found
for the given subreddit, the function should return None.

 """

import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recurse"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, params={'limit': 100, 'after': after},
                     allow_redirects=False,
                     headers={'user-agent': 'myUser'})

    if r.status_code == 200:
        data = r.json()
        for hotTopic in (data['data']['children']):
            hot_list.append(hotTopic['data']['title'])
        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
