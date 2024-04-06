import subprocess
from urllib.request import urlopen
import banners
import time

app_name = ""
repo_txt_link = ""


def update_client_version(v):
    with open("version.txt", "r") as vers:
        if vers.read() != v:
            return True
        else:
            return False


def main():
    try:
        version = (urlopen(repo_txt_link).read()).split("\n")[0]

    except Exception:
        print("[!] Unable to Fetch Origin version.txt     [!]")
        print("[!] Please Check Your Internet Connection! [!]")
        print("[*] Exiting ...                            [*]")
        quit()

    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return f"[+] Updated to latest version: v{version}.. [+]"

    else:
        return "[*] You are already up to date [*]"


if __name__ == '__main__':
    print(f"[*] Welcome to {app_name} Auto Updater [*]")
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print("[*] Note : Git must be installed to use updater.py [*]")
    time.sleep(5)
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"[*] Checking {app_name} version information..    [*]")
    print(main())
    print("[*] Exiting ... [*]")
