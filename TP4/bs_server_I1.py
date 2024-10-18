import socket
import sys

host = '10.1.1.1'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)

conn, addr = s.accept()

print('connected by : ', addr)

while True :
    try:
        data = conn.recv(1024)
        if not data : break
        print(f"Donnees recues du client :  {data}")
         
        conn.sendall(b"Salut mec.")

    except socket.error:
        print("Error Occured.")
        break

conn.close()

sys.exit(0)