import os
from cryptography.fernet import Fernet


class Decrypter:
    def __init__(self,
                secret_key,
                files_dict,
                files
                ) -> None:
        
        self.secret_key = secret_key
        self.files_dict = files_dict
        self.files = files

    def decrypt(self) -> None:
        for _ in self.files:
            if _ == '.DS_Store':
                continue

            if _ in self.files_dict:
                os.rename(_, self.files_dict[_])

            with open(_, "rb") as the_file:
                contents = the_file.read()

            contents_decrypted = Fernet(self.secret_key).decrypt(contents)

            with open(_, "wb") as the_file:
                the_file.write(contents_decrypted)


start = Decrypter()
start.decrypt()
