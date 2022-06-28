import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 10002))
print('conectado')

namefile=str(input('nome: '))
client.send(namefile.encode())

with open (namefile, 'wb')as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

