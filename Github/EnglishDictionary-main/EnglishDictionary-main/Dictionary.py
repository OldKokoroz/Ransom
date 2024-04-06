
import json
import time
from difflib import get_close_matches as match

data = json.load(open("data.json"))


# Word Function

def dictionary(word):
    word = word.lower()

    if word in data:
        return data[word]

    # Word Match in case
    elif len(match(word, data.keys(), cutoff=0.8)) > 0:
        time.sleep(1)
        answer = input(f"\nDid you mean {match(word, data.keys())[0]}  Y/N : ")

        if answer == "Y" or "y":
            return data[match(word, data.keys())[0]]

        elif answer == "N" or "n":
            time.sleep(1)
            return "The word doesn't exist!"

        else:
            time.sleep(1)
            return "\nError!\n"

    else:
        time.sleep(1)
        return "\nThe word doesn't exist!"


# Word Output

word = input("\nEnter word: ")
output = dictionary(word)

# Printing with index

if type(output) == list:
    time.sleep(1)
    print(f"\nMeanings of {word} :")

    for i in range(len(output)):
        print(f"\n{i} - {output[i]}")
        time.sleep(1)

else:
    time.sleep(1)
    print(f"Mean : \n 0 - {output}")
