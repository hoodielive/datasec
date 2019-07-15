#!/usr/bin/env python3

import subprocess
import optparse

def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}.')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
        
# parser object/entity 
parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='interface to change MAC address.')
parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
(options, arguments) = parser.parse_args()

# ui
change_mac(options.interface, options.new_mac)
