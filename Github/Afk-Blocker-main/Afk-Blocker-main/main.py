import subprocess


cmd = "pip install -r requirements.txt"

p2 = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p2.wait()

if p2.returncode == 0:
    print("\nRequirements | Successful ✔ ")
else:
    print("\nRequirements | Failed ✘ ")


process = subprocess.call(['Python', 'afk_blocker.py'])