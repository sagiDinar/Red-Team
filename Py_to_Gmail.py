import smtplib  # Importing smtplib for SMTP communication
import ssl  # Importing ssl for secure socket layer
import os  # Importing os for environment variables

# Description: Sending an email using SMTP with Python

smtp_server = 'smtp.gmail.com'
port = 465
# Change This!
sender = 'thesenderemail@gmail.com'

# Description:
# Go to your Gmail account, enable 2-factor authentication, and then create an app password.
# This unique password will be retrieved from the environment variable set in the command prompt.
# Open cmd command prompt, and save the password as an environment variable.
# Don't forget to run this script from the same cmd window.

password = os.getenv('EMAIL_PASSWORD')  # Retrieve password from environment variable
# Change This!
receiver = 'thereceiveremail@gmail.com'
message = """\
From: {}
To: {}
Subject: Hi There! From Python Bot

This message was sent from Python!
""".format(sender, receiver)

context = ssl.create_default_context()

# Establishing a secure SMTP connection
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)  # Logging in to the SMTP server
    # Sending email
    server.sendmail(sender, receiver, message)
