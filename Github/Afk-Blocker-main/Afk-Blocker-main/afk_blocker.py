#!/usr/bin/env python

# afk blocker (mouse-mover)
# works on only Linux and Windows

import random, sys
import time, keyboard
from time import localtime, strftime
import pyautogui as pag

while True:
    try:
        d = strftime("%H:%M", localtime())

        time.sleep(1)
        print(f"\n                            Current time is : {d}")

        def running_time():
            while True:
                global e
                time.sleep(1)
                e = input("\nMinutes to Run (Default : 10min): ") or (int(10))
                if float(e) >= float(5):
                    time.sleep(2)
                    print("\n       Alright, on the way")
                    break
                elif float(e) == 0:
                    print("\n       Invalid number!")
                else:
                    print("\n    We recommend at least 5min")

        running_time()

        time.sleep(2)
        user_input_time = input("\nTime between mouse moves (second): ")

        if float(user_input_time) >= float(1):
            print(f"\n      Good choice : {user_input_time} sec")
            time.sleep(3)
            print("\n    __ It's happening baby __")
            while True:
                listoto=("w", "a", "s", "d")
                    
                def auto_both():
                    x = random.randint(500, 700)
                    y = random.randint(200, 600)
                    pag.moveTo(x, y, 0.5)
                    time.sleep(float(user_input_time))
                    time.sleep(1)
                        
                    pag.press(listoto, 1, 1 )


                auto_both()

                f = strftime("%H:%M", localtime())
                start_time = int(d[3:5])
                finish_time = int(f[3:5])
                if finish_time - start_time == int(e):
                    print(f"""
                        Start  Time : {d}
        
                        Finish Time : {f}
        
                        Time   Past : {e} min
                    """)
                    time.sleep(1)
                    sys.exit(0)
        else:
            print("\n   Choose a number greater than 1 !")

    except KeyboardInterrupt:
        print("\n\n   Hope to see you again\n")

    time.sleep(1)
    print("\n********************************END********************************\n")
    sys.exit(0)