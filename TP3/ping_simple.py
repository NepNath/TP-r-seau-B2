import os
ping = os.popen('ping -n 1 8.8.8.8')
for line in ping.readlines():
    print(line)


#os.popen() ça récupère ce que tu met dans la string en argument (donc une commande shell)
#et sa stock le résultat (si tu l'a foutu dans une variable)