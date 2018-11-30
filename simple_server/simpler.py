#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import socket

HOST = "127.0.0.1"
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    
    connection, addr = sock.accept()
    with connection:
        print("Connection from ", addr)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(data.decode())
            connection.sendall(data)
