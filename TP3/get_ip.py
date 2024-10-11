import psutil
import socket
import ipaddress

def get_ipv4_address(): #c'éation de la fonction qui récupère l'ipv4
    interfaces = psutil.net_if_addrs()  #récupère et stoque dans la fonction "interfaces" les données de ma carte réseau (adresse ip, mac etc...)
    
    for interface_name, addresses in interfaces.items(): #création d'une boucle qui va parcourir chaque donnée dans ma listes précédente et utiliser "addresses" comme alias 
        for address in addresses: #même chose que au dessus en soit mais scan les adresses 
            if address.family == socket.AF_INET:  # Vérifie si il y a une adresse IPv4 (grace au package socket) si c'en est bien une 
                ip = address.address # stock l'ipv4 dans une variable "ip" gracce à address.address (l'un est le nom d'alias et l'autre permet de dire que tu cherche l'ip)
                netmask = address.netmask #même chose que l'ip mais avec le netmask, la commande aide à comprendre comment récupérer des éléments précis (par exemple )
                return ip, netmask # retourne les deux éléments pour la suite 

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
