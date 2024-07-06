#!/usr/bin/python3

import socket
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.settimeout(5)

# host = "2001:41d0:8:ccd8:137:74:187:101" #Lets check it out, this is HACKTHISWEBSITE.org
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(portParameter):
    if s.connect_ex((host, portParameter)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
