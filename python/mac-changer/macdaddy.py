#!/usr/bin/env python3

import subprocess
interface = input("interface > ")
#interface = "wlan0"
state =['down', 'up']
new_mac = input("new Mac > ")

print(f'[+] Changing MAC address for {interface} to {new_mac}.')
subprocess.call(f'ifconfig {interface} {state[0]}', shell=True)
subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
subprocess.call(f'ifconfig {interface} {state[1]}', shell=True)
