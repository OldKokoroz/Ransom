from time import sleep
import os
from dicts import alphabet, reverse_alp


class TurningFunc:
    def __init__(self, translated="", as_text=""):
        self.translated = translated
        self.as_text = as_text

    def mode1(self):
        # Text - Code Section
        while True:
            message = input("""
-------------------------------------
Message: """).lower()

            if message == "99":
                break

            for inp in list(message):
                if inp in alphabet.keys():
                    print("\nChange mode to translate morse code!\n")
                    break

                elif inp not in reverse_alp.keys():
                    print(f"---> Invalid character! {inp}")
                    break

                self.translated += inp

                self.as_text += f"{reverse_alp.get(inp)}/"

                os.system(f"say {inp}")

                sleep(0.05)

            print(f"""\n
Morse Code: {self.as_text}
-------------------------------------""")

            os.system(f"say your message is {self.translated}")
            self.as_text = ""
            self.translated = ""

    def mode2(self):
        # Code - Text Section
        while True:
            code = input("""\n
-------------------------------------
Morse Code (Ex: ••••/–––/•) : """).split("/")

            for _ in code:
                if _ not in alphabet.keys():
                    print("!!! Invalid characters included !!!")

                self.as_text += f"{alphabet.get(_)}"

                os.system(f"say {alphabet.get(_)}")

                sleep(0.1)

            os.system(f"say your message is {self.as_text}")
            print(f"""\n
Message: {self.as_text.capitalize()}
-------------------------------------
""")
            self.as_text = ""

    def for_cli(self):
        while True:
            try:
                sleep(1)

                mode = input('''
|----------MODE-----------|
| 1 - Text -> Morse code  |
| 2 - Text <- Morse code  |
| 99 - Exit               |
|-------------------------|
|-> ''')

                if mode == "1":
                    self.mode1()

                elif mode == "2":
                    self.mode2()

                elif mode == "99":
                    print("Exiting...")
                    exit(0)

                else:
                    print("Invalid input!")
                    exit(1)

            except ValueError or Exception:
                print("Error!")

            except KeyboardInterrupt:
                print("Exiting")
                exit()


TurningFunc().for_cli()
