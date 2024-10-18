import socket
import sys

host = '10.1.1.1'  

port = 13337           

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
while True : 
    print(f"Connection à {host} réussie avec le port {port}")
    try :
        data = s.recv(1024)
        if not data : break
        print(f"Donnees recues du client :  {data}")
    

    except socket.error: 
        print("Sorry, an error Occured")
        break


s.sendall(b'Meooooo !')

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu {repr(data)}")

sys.exit(0)
