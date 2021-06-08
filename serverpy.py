#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20 
#Creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding to particular port and IP
s.bind((TCP_IP, TCP_PORT))
#listening on port
s.listen(1)
#Accepting connection from client
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	iif not data: break
	print "received data:", data
	conn.send(data)  # echo
conn.close()
