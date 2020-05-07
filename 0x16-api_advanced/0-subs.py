#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    r = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if r.status_code != 200:
        return 0

    subscribers = r.json().get("data").get("subscribers")
    return subscribers
