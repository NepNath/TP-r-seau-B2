import psutil
import socket
import ipaddress

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
