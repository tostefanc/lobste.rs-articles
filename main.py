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


def remove_duplicates_article(input_raw):
    result = {}

    for key, value in input_raw.items():
        print("IN FOR: ", input_raw[key])
        if value not in result.values():
            result[key] = value
    return result


def recreate_articles_json():
    if exists(articles_file):
        os.remove(articles_file)
        # big_soup = lobster_req.format_lobster_articles() | hacker.get_hacker_object()
        big_soup = hacker.get_hacker_object() | lobster_req.format_lobster_articles()
        # big_soup_no_duplicates = remove_duplicates_article(big_soup)
        # json_big_soup = json.dumps(big_soup_no_duplicates)
        json_big_soup = json.dumps(big_soup)

        with open("articles.json", 'w', encoding='utf-8') as f:
            f.write(json_big_soup)
            f.close()
    else:
        # big_soup = lobster_req.format_lobster_articles() | hacker.get_hacker_object()
        big_soup = hacker.get_hacker_object() | lobster_req.format_lobster_articles()
        # big_soup_no_duplicates = remove_duplicates_article(big_soup)
        # json_big_soup = json.dumps(big_soup_no_duplicates)
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
