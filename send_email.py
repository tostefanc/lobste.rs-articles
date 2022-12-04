#!/usr/bin/env python3

import smtplib
import ssl
from email.message import EmailMessage
import jinja2
import sec

subject_of_email = "sec.py testing"
obj = {
    'el1': {
    'title': '&#8216;Let It Crash&#8217; under attack',
    'link': 'http://blog.syncpup.com/posts/let-it-crash-under-attack.html'
    },

    "el2": {
    'title': 'How Do Software Projects End?',
    'link': 'https://danielbmarkham.com/how-do-software-projects-end/'
    },

    "el3" : {
    'title': 'Tailwind is a Leaky Abstraction',
    'link': 'https://jakelazaroff.com/words/tailwind-is-a-leaky-abstraction/'
    }
}

# body = """

# <a href="http://blog.syncpup.com/posts/let-it-crash-under-attack.html">&#8216;Let It Crash&#8217; under attack</a> <br>
# <a href="https://blog.phundrak.com/emacs-29-what-can-we-expect/">Emacs 29 is nigh! What can we expect?</a>
# """
body = "taking the pass and the receiver, sender from the sec.py"

# for e in obj: 
#     # body += """
#     #     <a href="{e.link}">{e.title}</a> <br>
#     # """
#     print(f"Link: e['link'] ")


print(f"Sender: {sec.email_sender}, password is {sec.email_sender_password}, receiver: {sec.email_receiver}")

em = EmailMessage()
em['From'] = sec.email_sender
em['To'] = sec.email_receiver
em['Subject'] = subject_of_email
em.add_header('Content-Type','text/html')
# em.set_content(body)
em.set_payload(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sec.email_sender, sec.email_sender_password)
    smtp.sendmail(sec.email_sender, sec.email_receiver, em.as_string())
 