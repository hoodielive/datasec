#!/usr/bin/env python3

import subprocess
interface = "wlan0"
state =['down', 'up']
new_mac = "00:22:33:44:55:77"

print(f'[+] Changing MAC address for {interface} to {new_mac}.')

subprocess.call(f'ifconfig {interface} {state[0]}', shell=True)
subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
subprocess.call(f'ifconfig {interface} {state[1]}', shell=True)
