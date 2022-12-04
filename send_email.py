#!/usr/bin/env python3

import smtplib
import ssl
from email.message import EmailMessage
import sec #Local secrets
import json
from datetime import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


today_date = dt.today().strftime('%d-%m-%Y')
subject_of_email =f"Lobste.rs articles from: {today_date}"

body = ''

with open('articles.json') as user_file:
  articles_contents = user_file.read()

articles_dict = json.loads(articles_contents)

for key, article in articles_dict.items():
    # print(f"KEY: {key}  Titles: {article['title']} LINKS: {article['link']}")
    body += f"<p>{key}. <a href={article['link']}>{article['title']}</a></p>"

# print(json.dumps(articles_dict, indent = 4,))

# print( type(body))

def send_the_lobster_articles(body_contents):
    em = MIMEMultipart()
    em['From'] = sec.email_sender
    em['To'] = sec.email_receiver
    em['Subject'] = subject_of_email
    # em.add_header('Content-Type','text/html')
    em.attach(MIMEText(body, "html"))
    
    # em = EmailMessage()
    # em['From'] = sec.email_sender
    # em['To'] = sec.email_receiver
    # em['Subject'] = subject_of_email
    # em.add_header('Content-Type','text/html')
    # em.set_content("{}".format(body_contents))
    # em.set_payload(body_contents)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sec.email_sender, sec.email_sender_password)
        smtp.sendmail(sec.email_sender, sec.email_receiver, em.as_string())

send_the_lobster_articles(body)