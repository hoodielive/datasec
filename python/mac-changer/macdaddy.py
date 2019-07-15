#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    # UI parser object/entity 
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='interface to change MAC address.')
    parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an new_mac, use --help for more info.")
    else: 
    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}.')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
        
#(options, arguments) = get_arguments()
options = get_arguments()
change_mac(options.interface, options.new_mac)
