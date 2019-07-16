#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    # UI parser object/entity 
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='interface to change MAC address.')
    parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    (options, arguments) = parser.parse_args()

    # check to see if proper args are supplied
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an new_mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}.')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
        
options = get_arguments()

ifconfig_result = subprocess.check_output(["ifconfig", options.interface]) 
mac_addr_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result.decode('utf-8'))
if mac_addr_search_result:
    print(mac_addr_search_result.group(0))
else:
    print('[-] Could not read MAC')
