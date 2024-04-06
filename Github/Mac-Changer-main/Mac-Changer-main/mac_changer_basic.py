import subprocess
import Logo

print(Logo.logo)

print("\nMac_Changer Started!")

interface = str(input("\nEnter the interface of the mac you want to change: "))

mac_address = str(input("\nEnter a mac address: "))


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])


print("\nMac address of your", interface, "successfully changed to ", mac_address)
