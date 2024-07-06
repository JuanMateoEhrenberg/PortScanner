#!/usr/bin/python3

import socket

def banner(ip, port):
    socketObj = socket.socket()
    socketObj.connect((ip, int(port)))
    socketObj.settimeout(5)
    print(str(socketObj.recv(1024)).strip('b')) #Cleans output, example only, should be better programmed.

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()