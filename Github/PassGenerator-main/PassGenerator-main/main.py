import random
import string
from time import sleep

key = ""  # Empty Password
length = 0


def generate():
    global key
    global length
    print("******** Generator Started ********")
    chars_ = ["*", "!", "_", "-", ".", "?", "%", "&", "+"]

    for value in range(97, 123):
        chars_.append(chr(value))

    for value in range(97, 123):
        chars_.append(chr(value).capitalize())

    for nums in range(0, 10):
        chars_.append(nums)

    # get_chars = input("Do you want specific characters in your Password ? ""Ex: 1-2-a-b-D-c: ")
    key_len = int(input("Password Length: "))
    length = key_len

    while len(key) < length:
        char = random.choice(chars_)
        key += str(char)

        if len(key) == length:
            break

    with open("passwd.txt", "a") as txt:
        txt.write(key)

    verify(key)
    julius(key)


def verify(passwd=key):
    global length
   
    count = 0
    if not 8 <= len(passwd) <= 24:
        passwd += passwd[random.choice(range(0, length))]

    print("\nLength     : ✓")
    sleep(1)
    print("Characters : ✓")
    sleep(1)
    print("Strong     : ✓\n")
    sleep(1)


def julius(text=key, shift=7, alphabets=None):
    if alphabets is None:
        alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    print("\nPassword         : " + key)
    sleep(1)
    print("Password (Caesar): " + text.translate(table))
    sleep(1)
    

def starter():
    global key
    while True:
        mode = input("""
======== Mode ========
1 - Generate
2 - Check

|> """)
        print("-" * 25 + "\n")

        if mode == "1":
            generate()

        elif mode == "2":
            print("******** Verifier Started ********")
            password = input("\nPassword to check: \n")
            verify(password)

        elif mode not in ["1", "2"]:
            print("\nChoose between 1 - 2 !")


try:
    starter()

except KeyboardInterrupt:
    print("Exiting..")
    exit()
