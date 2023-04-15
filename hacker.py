#!/usr/bin/env python3
import sys
import requests

headers = {
    'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }

url_top_stories = 'https://hacker-news.firebaseio.com/v0/topstories.json'
top_stories = []


def get_hacker_object():
    def hk_get_top_stories():
        try:
            stories = requests.get(url_top_stories, headers=headers).json()
        except Exception as e:
            sys.exit(e)
        return stories

    for story in range(0, 24):
        url = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(hk_get_top_stories()[story])

        top_stories.append(
            requests.get(url, headers=headers)
            .json()
        )

    hacker_object = {
        i: {
            'title': top_stories[i]['title'],
            'link': top_stories[i]['url']
        } for i in range(len(top_stories))
    }

    return hacker_object


get_hacker_object()

