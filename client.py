import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8820))
data = client_socket.recv(1024).decode('utf-8')
print(data)