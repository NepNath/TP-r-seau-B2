import os
import subprocess
from sys import argv

addr = argv[1]


res = subprocess.run(['ping', '-n', '4', addr], capture_output=True, text=True)

if res.returncode != 0 : 
    if "Name or service not known" in res.stderr:
            print(f"Erreur : L'adresse '{addr}' existe po")
    elif "Destination Host Unreachable" or "Request timed out" or "100% packet loss" in res.stdout:
         print("DOWN ! ⬇️")
else :
        print("UP ! ⬆️")
        
    