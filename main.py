#!/usr/bin/env python3

import lobster_req
import os
import json
import time
from send_email import send_the_lobster_articles
from os.path import exists
import hacker

articles_file = "articles.json"


def is_articles_json_old(days=1):
    articles_file_timestamp = os.path.getmtime(articles_file)
    if (time.time() - articles_file_timestamp) / 3600 > 24*days:
        return True


def recreate_articles_json():
    if exists(articles_file):
        os.remove(articles_file)
        big_soup = lobster_req.format_lobster_articles() | hacker.get_hacker_object()
        json_big_soup = json.dumps(big_soup)

        with open("articles.json", 'w', encoding='utf-8') as f:
            f.write(json_big_soup)
            f.close()
    else:
        big_soup = lobster_req.format_lobster_articles() | hacker.get_hacker_object()
        json_big_soup = json.dumps(big_soup)

        with open("articles.json", 'w', encoding='utf-8') as f:
            f.write(json_big_soup)
            f.close()


def format_the_email_body():
    body = ""
    with open('articles.json') as user_file:
        articles_contents = user_file.read()

    articles_dict = json.loads(articles_contents)

    for key, article in articles_dict.items():
        body += f"<p>{key}. <a href={article['link']}>{article['title']}</a></p>"
    return body


if not exists(articles_file):
    recreate_articles_json()

if is_articles_json_old():
    print("old file")
    recreate_articles_json()
    print("file has been removed")
    send_the_lobster_articles(format_the_email_body())
    print("email has been sent")
else:
    send_the_lobster_articles(format_the_email_body())
    print("good to go")
