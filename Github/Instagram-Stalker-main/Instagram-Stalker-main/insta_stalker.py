from instabot import Bot
import sys, pwinput, keyboard

try:

    stalker_acc = Bot()

    print("\n ---------------------------")

    while True:
        try:
            x = input("\n Username of the Account : ")

            y = pwinput.pwinput(prompt = "\n Password of the Account: ", mask = "*")

            if len(x) and len(y) < int(5):
                print("\n     Invalid credentials")
                break
                
            else:
                print("\n Validating Credentials\n")
        except:
            break
        print(" ---------------------------\n")

        stalker_acc.login(username=f"{x}", password=f"{y}")

        victim = input(" Username of the victim : ")

        followers = stalker_acc.get_user_followers(victim)

        for follower in followers:
            print(

                stalker_acc.get_user_info(follower)

            )

except KeyboardInterrupt:
    print("""

    >>> Goodbye, Hope to see you again. <<<

    """)
    sys.exit(0)