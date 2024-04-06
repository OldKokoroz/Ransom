import time, re, subprocess, optparse


def get_inputs():
    my_parse = optparse.OptionParser()

    my_parse.add_option("-i", "--iface", dest="interface", help="Enter Interface to change")
    my_parse.add_option("-m", "--mac", dest="new_mac", help="Enter New Mac")

    """
    my_parse.add_option("-h", "--help", dest="func_help", help="-h or --help to see how to use")
    
    func_help = '''\n
    -i , --iface == Interface to change
            interfaces : wlan0 , eth0 , en0 ...

    -m , --mac   == New Mac
            !! Do not use 11:xx:xx:xx:xx:xx
            Gives Error on every device
    \n'''
    """

    return my_parse.parse_args()


def using_terminal(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def last_check(interface):
    check = subprocess.check_output("ifconfig", interface)

    mac_check = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(check))

    if mac_check:
        return mac_check.group(0)

    else:
        return "Mac Check Error"


time.sleep(2)
print("\n-------- MAC CHANGER STARTED --------\n")
time.sleep(3)

(user_input, arguments) = get_inputs()
using_terminal(user_input.interface, user_input.new_mac)
final_mac = last_check(user_input.interface)


if final_mac == str(user_input.new_mac):
    print(f"""\n
    -------------------------------------\n
    Interface : {str(user_input.interface)}  \n
      Old Mac : {last_check(str(user_input.interface))}  \n
      New Mac : {str(user_input.new_mac)} \n
    -------------------------------------\n
    """)

else:
    print("Program Didn't Work Mate")
