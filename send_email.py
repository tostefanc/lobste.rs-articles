#!/usr/bin/env python3

import smtplib
import ssl
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
    body += f"<p>{key}. <a href={article['link']}>{article['title']}</a></p>"

def all_receivers():
    if type(sec.email_receiver is list):
        receivers = ', '.join(sec.email_receiver)
    else:
        receivers = sec.email_receiver
    return receivers

def send_the_lobster_articles(body_contents):
    em = MIMEMultipart()
    em['From'] = sec.email_sender
    em['To'] = all_receivers()
    em['Subject'] = subject_of_email
    em.attach(MIMEText(body_contents, "html"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sec.email_sender, sec.email_sender_password)
        smtp.sendmail(sec.email_sender, sec.email_receiver, em.as_string())

send_the_lobster_articles(body)