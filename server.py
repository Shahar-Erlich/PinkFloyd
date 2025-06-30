import socket
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 8820))
server_socket.listen()
(client_socket, client_address) = server_socket.accept()

print("Client Connected!")
client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
