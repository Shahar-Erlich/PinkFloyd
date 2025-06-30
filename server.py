import socket
import data
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)

def handleClient():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break;
        if data == 'exit':
            client_socket.close()
        print("from connected user: " + str(data))

data.createDataBase()
server_socket.bind(CONNECTION)
server_socket.listen()
(client_socket, client_address) = server_socket.accept()

print("Client Connected!")
client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
handleClient()


