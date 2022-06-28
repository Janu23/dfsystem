from http import server
import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', '10000'))

conn, addr = server.accept()
namefile = conn.recv(1024).decode

with open(namefile, 'rb') as file:
    for data in file.readlines():
        conn.send(data)
    
