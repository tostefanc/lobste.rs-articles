## lobste.rs articles 

This program is grabbing articles from lobste.rs RSS page and is sending them as an email

In order to use this script you need to first install the requirements: 

```sh
pip install -r requirements.txt
```

The email sender, email sender password and email receiver or receivers need to be in a file called sec.py
If you want to have multiple receivers, you need to put all email addresses in a list

Example with one receiver:
```python
#!/usr/bin/env python3

email_sender = "example_sender@gmail.com"
email_sender_password = "sssenderpassword123"
email_receiver = "example_receiver@gmail.com"
```

Example with multiple receivers:
```python
email_sender = "example_sender@gmail.com"
email_sender_password = "sssenderpassword123"
email_receiver = ["example1_receiver@gmail.com", "example2_receiver@gmail.com", "example3_receiver@gmail.com"]
```