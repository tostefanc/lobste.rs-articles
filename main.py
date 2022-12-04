#!/usr/bin/env python3

import lobster_req
import os.path as path
import json
import time

def is_articles_json_old(days=1): 
    articles_file = path.getmtime("articles.json") 
    
    if not (time.time() - articles_file) / 3600 > 24*days:
        soup_object = lobster_req.format_lobster_articles()
        json_soup = json.dumps(soup_object)
        print(f"THE JSON SOUP: {json_soup}")
        with open("articles.json",'w',encoding = 'utf-8') as f:
            f.write(json_soup)
            f.close
