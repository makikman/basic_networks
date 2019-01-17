#!/usr/bin/env python
import requests
import socket
import sys
"""
An HTTP client using a traditional HTTP library (like Ruby's net/http) and one using sockets only that allows you to send basic GET and POST requests.
An HTTP client that supports SSL (both with HTTP library and with socket only).
An HTTP client that supports cookies (both with HTTP library and with socket only)
"""

ADDRESS = sys.argv[3]

def usage():
    print("Usage: %s [method options: -hg -hp -sg -sp] [extra options: -s -c -b -n] [Address]" % (sys.argv[0],))
    print("[Method options: First letter h for http and s for socket. Second letter g for get and p for post")
    print("Extra options: -s for ssl, -c for cookies, -b for both, -n for neither")


def http_request(method_flag, extra_flag):
    if method_flag[2] == 'g':
        r = requests.get(ADDRESS)
    elif method_flag[2] == 'p':
        r = requests.post(ADDRESS)
    else:
        usage()
        exit()
    print(r.text)
    if extra_flag[1] == 'c':
        print(r.cookies)
    

def socket_request(method_flag, extra_flag):
    if method_flag[2] == 'g':
        request = "GET / HTTP/1.1\nHost: %s\n\n" % (ADDRESS,)
        print(request)
    elif method_flag[2] == 'p':
        request = "POST / HTTP/1.1\nHost: %s\n\n" % (ADDRESS,)
    else:
        usage()
        exit()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ADDRESS, 80))
    s.sendall(request.encode())
    print(s.recv(4096).decode())
    s.close()


def main():
    if len(sys.argv) < 4:
        usage()
        exit()

    method_flag = sys.argv[1]
    extra_flag = sys.argv[2]

    if method_flag[1] == 'h':
        http_request(method_flag, extra_flag)
    elif method_flag[1] == 's':
        socket_request(method_flag, extra_flag)

main()