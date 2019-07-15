#!/usr/bin/env python3

import subprocess
import optparse

# parser object/entity 
parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='interface to change MAC address.')
parser.parse_args()

# ui
interface = input("interface > ")
new_mac = input("new Mac > ")

print(f'[+] Changing MAC address for {interface} to {new_mac}.')

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
