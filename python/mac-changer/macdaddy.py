#!/usr/bin/env python3

import subprocess
interface = input("interface > ")
state =['down', 'up']
new_mac = input("new Mac > ")

print(f'[+] Changing MAC address for {interface} to {new_mac}.')
subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
