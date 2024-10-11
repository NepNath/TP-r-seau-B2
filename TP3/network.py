import os
import subprocess
from sys import argv
import re
import socket
import psutil
import socket
import ipaddress
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def url_check(url):

    url_regex = re.compile(
        r'^(https?:\/\/)?'  
        r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6})'  
        r'(\/[a-zA-Z0-9_.-]*)*\/?$'  
    )
    

    return re.match(url_regex, url) is not None
    
def lookup(): #log fait
    fp = open(r'C:\Windows\Temp\network.txt', 'a')
    fp.write(f'{date} [INFO] Command <{argv[1]}> called with "{argv[2]}" \n')
    fp.write('.\n')   

    if len(argv) < 3: 
        print("errrur : pas assez d'argument (hostname)")
        fp.write("errrur : pas assez d'argument (hostname) \n")
        fp.write('.\n')
        return
    
    hstnm = argv [2]

    if url_check(hstnm) == True:
        ipaddr = socket.gethostbyname(hstnm)
        print(ipaddr)
        fp.write(f'{ipaddr} \n')
        fp.write('.\n')
    else : 
        print("erreur URL")
        fp.write("erreur URL \n")
        fp.write('.\n')
    fp.write(f'{date} [INFO] Command <lookup> was called successfully with "{argv[2]}"\n')
    fp.write('--- \n')
    fp.close

########

def ping():
    fp = open(r'C:\Windows\Temp\network.txt', 'a')
    fp.write(f'{date} [INFO] Command <{argv[1]}> called with "{argv[2]}" \n')
    fp.write('.\n')

    if len(argv) < 3: 
        print("errrur : pas assez d'argument (hostname)")
        fp.write('Argument error \n')
        fp.write('.\n')
        return
    
    addr = argv[2]

    res = subprocess.run(['ping', '-n', '4', addr], capture_output=True, text=True)

    if res.returncode != 0:
        print(f"Erreur : Impossible de joindre l'adresse '{addr}'")
        fp.write(f"error : {addr} isn't joinable")
        fp.write('.\n')
    else:
        if any(err_msg in res.stdout for err_msg in ["Destination host unreachable", "Request timed out", "100% packet loss"]):
            print("DOWN ! ⬇️")
            fp.write('Command output : "DOWN !" \n ')
            fp.write('.\n')
        else:
            print("UP ! ⬆️")
            fp.write('Command output : "UP !"\n')
            fp.write('.\n')
        fp.write(f'{date} [INFO] Command <lookup> was called successfully with "{argv[2]}"\n')
    fp.write('--- \n')
    fp.close
 
#########

def ip():
    fp = open(r'C:\Windows\Temp\network.txt', 'a')
    fp.write(f'{date} [INFO] Command <{argv[1]}> called with "{argv[2]}" \n')
    fp.write('.\n')

    def get_ipv4_address():
        interfaces = psutil.net_if_addrs()
        
        for interface_name, addresses in interfaces.items():
            for address in addresses:
                if address.family == socket.AF_INET:  # Vérifie si c'est une adresse IPv4
                    ip = address.address
                    netmask = address.netmask
                    return ip, netmask

    def calculate_network_info(ip, netmask):
        # Créer un objet réseau IPv4 à partir de l'IP et du masque de sous-réseau
        network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
        
        # Calculer le nombre d'adresses disponibles dans le sous-réseau
        available_addresses = network.num_addresses
        
        # Obtenir l'IP au format CIDR (par exemple, 192.168.1.29/24)
        cidr = network.with_prefixlen
        
        return cidr, available_addresses

    # Récupérer l'adresse IPv4 et le netmask
    ipv4_address, netmask = get_ipv4_address()

    # Calculer l'adresse au format CIDR et le nombre d'adresses disponibles
    cidr_address, available_addresses = calculate_network_info(ipv4_address, netmask)

    # Afficher les résultats
    print(cidr_address)
    print(available_addresses)
    fp.write(f'{cidr_address} \n')
    fp.write(f'{available_addresses} \n')
    fp.write(f'{date} [INFO] Command <lookup> was called successfully with "{argv[2]}"\n')
    fp.write('--- \n')
    fp.close

if len(argv) < 2:
    print("Erreur : Aucune commande fournie (lookup, ping, ip)")
else:
    command = argv[1]
    
    if command == "lookup":
        lookup()
    elif command == "ping":
        ping()
    elif command == "ip":
        ip()
    else:
        print(f"Erreur : Commande '{command}' non reconnue. Utilisez 'lookup', 'ping', ou 'ip'")