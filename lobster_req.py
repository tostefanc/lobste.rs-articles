#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
import sys

headers = {
    'USER-AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0' 
    }
lobster_url = 'https://lobste.rs/rss'
soup_titles = []
soup_links = []

def get_lobster_articles():

    try:
        lobster_request = requests.get(lobster_url, headers=headers)
        
    except Exception as e:
        sys.exit(e)
    
    return lobster_request

def format_lobster_articles():
    lobster_request = get_lobster_articles()
    lobster_soup = bs(lobster_request.text, 'lxml-xml')

    soup_ingredients = lobster_soup.find_all('item')

    for item in soup_ingredients:
        soup_titles.append(item.title.text)
        soup_links.append(item.link.text)

    soup_object = {
        i : {
            'titleLOBSTER': soup_titles[i],
            'link': soup_links[i]
            } for i in range(len(soup_ingredients))
        }
    
    return soup_object