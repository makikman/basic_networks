#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import socket

HOST = "127.0.0.1"
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while(True):
        message = input("enter message: ")
        sock.sendall(message.encode())
        data = sock.recv(1024)
        print(data.decode())


        

