import socket
import os
from sys import argv
import re

def url_check(url):

    url_regex = re.compile(
        r'^(https?:\/\/)?'  
        r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6})'  
        r'(\/[a-zA-Z0-9_.-]*)*\/?$'  
    )
    

    return re.match(url_regex, url) is not None

hstnm = argv [1]

if url_check(hstnm) == True:
    ipaddr = socket.gethostbyname(hstnm)
    print(ipaddr)
else : 
    print("erreur URL")

