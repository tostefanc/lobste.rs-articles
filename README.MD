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
## Dockerfile has been added so it can also run in docker now: 

- After cloning the repository make sure you created the sec.py file (see above) 
> Note: if you plan to use a `Gmail` address to send the email you need to enable [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) and use this instead of your password
- Finally, you just need to execute the lobsters-cron.sh script (make sure it's executable)

```sh 
chmod +x lobsters-cron.sh
```

```sh
./lobsters-cron.sh
```

- To run the bash script in cron you need to specify the `lobste.rs-articles` directory (can be done via a subshell). Example for a cron that's running everyday at 14:00: 
```sh
0 14 * * * (cd /full/path/to/lobste.rs-articles/ && ./lobsters-cron.sh)
```
