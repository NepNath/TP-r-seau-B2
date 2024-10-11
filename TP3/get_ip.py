import psutil
import socket

def get_ipv4_address():
    interfaces = psutil.net_if_addrs()
    
    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if address.family == socket.AF_INET:  
                return address.address, address.netmask



ipv4_address = get_ipv4_address()

print(ipv4_address)