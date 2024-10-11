import socket
import os
from sys import argv

hstnm = argv [1]


ipaddr = socket.gethostbyname(hstnm)

print(ipaddr)