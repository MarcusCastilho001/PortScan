
#By: Marcus Castilho (root@root)
#Date: 15/04/2020
#Atualização: 16/04/2020 - 16:46


import socket
from time import sleep

print ('''\033[01;031m
(  ____ )(  ___  )(  ____ )\__   __/(  ____ \(  ____ \(  ___  )( (    /|
| (    )|| (   ) || (    )|   ) (   | (    \/| (    \/| (   ) ||  \  ( |
| (____)|| |   | || (____)|   | |   | (_____ | |      | (___) ||   \ | |
|  _____)| |   | ||     __)   | |   (_____  )| |      |  ___  || (\ \) |
| (      | |   | || (\ (      | |         ) || |      | (   ) || | \   |
| )      | (___) || ) \ \__   | |   /\____) || (____/\| )   ( || )  \  |
|/       (_______)|/   \__/   )_(   \_______)(_______/|/     \||/    )_)
\033[m''')
print("                                By: Marcus Castilho (root@root)")
print("						[versão 2.1]")
print()
sleep(2)

dns = input("Dominio (ex: google.com ou IP): ").lower()
porta = int(input("Porta (ex: 80): "))


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(0.1)
codigo = cliente.connect_ex ((dns, porta))

if codigo == 0:
    print (porta, "OPEN")
else:
   print (porta, "Closed")
