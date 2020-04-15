#By: Marcus Castilho (root@root)
#Date: 15/04/2020


import socket
from time import sleep

print ('''
(  ____ )(  ___  )(  ____ )\__   __/(  ____ \(  ____ \(  ___  )( (    /|
| (    )|| (   ) || (    )|   ) (   | (    \/| (    \/| (   ) ||  \  ( |
| (____)|| |   | || (____)|   | |   | (_____ | |      | (___) ||   \ | |
|  _____)| |   | ||     __)   | |   (_____  )| |      |  ___  || (\ \) |
| (      | |   | || (\ (      | |         ) || |      | (   ) || | \   |
| )      | (___) || ) \ \__   | |   /\____) || (____/\| )   ( || )  \  |
|/       (_______)|/   \__/   )_(   \_______)(_______/|/     \||/    )_)
''')
sleep(1)
print("                                By: Marcus Castilho (root@root)")
print()
sleep(2)

dns = input("Dominio (ex: google.com): ")
porta = int(input("Porta (ex: 80): "))


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(0.1)
codigo = cliente.connect_ex ((dns, porta))

if codigo == 0:
   print (porta, "OPEN")
else:
   print (porta, "Closed")
