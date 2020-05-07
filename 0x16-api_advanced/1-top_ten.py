#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                     .format(subreddit),
                     headers={"User-Agent": "My-User-Agent"},
                     allow_redirects=False)
    posts = r.json().get('data', {}).get('children', {})
    if r.status_code != 200 or not posts:
        return print("None")
    for post in posts[0:10]:
        print(post.get('data', {}).get('title'))
