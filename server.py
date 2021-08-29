#!/usr/bin/python

import socket

lhost = "127.0.0.1"
lport = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((lhost, lport))
s.listen(2)
print(f"Listening for connections on IP: {lhost} Port: {lport}")
target, ip = s.accept()
print("Connectiong recived")


while True:
	command = raw_input("Shell#~ %s" % str(ip))
	target.send(command)
	if command == "!q":
		break
	result = target.recv(2048)

target.close()
s.close()

