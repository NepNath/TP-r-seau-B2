import os
from sys import argv

ping = os.popen(f'ping {argv[1]}')
for line in ping.readlines():
    print(line)