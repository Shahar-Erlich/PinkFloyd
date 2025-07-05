import select
import socket
import data #import the txt parser
import hashlib
import selectors

ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)
HASH_PASS = "0c9420a304a2267b42962a958c95609d" #Hashed Password
APPROVE_MESSAGE = "Correct!"
#check if user is still connected
connected = True

class Server:
    def __init__(self):
        self.selector = selectors.DefaultSelector()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inputs = [self.server_socket]
    def handle_client(self):
        '''function that handles user connections
           also receives the options from the users and returns the answers'''
        while self.inputs:
            readables,_,_ = select.select(self.inputs,[],[])
            for i in readables:
                if i is self.server_socket:
                    client_socket,address = self.server_socket.accept()
                    self.inputs.append(client_socket)
                    self.connect_user(client_socket,address)
                    client_socket.send(f"Welcome to server {address}!".encode())
                    print("Client connected!")
                else:
                    try:
                        data = i.recv(1024).decode('utf-8')
                        self.functions[data](i)
                        print(f"from {i}: " + str(data))

                    except Exception as e:
                        print(e)
                        self.inputs.remove(i)
                        print("Client Disconnected")
                        i.close()



    def open_server(self):
        # Parse the text file to structs
        data.parse_text_file()
        # bind server to address/port
        self.server_socket.bind(CONNECTION)
        print(f"[SERVER] Server binded to {CONNECTION}")
        # listen to client connections
        self.server_socket.listen()
        print("[SERVER] Server listening to port")
        self.handle_client()
        # wait to accept clients trying to connect

    def connect_user(self,client_socket,client_address):
        client_socket.send(f'Enter Password'.encode('utf-8'))
        # loop and check each time if the client sent the correct password
        while hashlib.md5(client_socket.recv(1024)).hexdigest() != HASH_PASS:
            client_socket.send(f'Enter Password'.encode('utf-8'))
        print("Client Connected!")
        connected = True
        # send welcome message to client
        client_socket.send(APPROVE_MESSAGE.encode('utf-8'))
        client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
        # handle client
        self.handle_client()

    # Get all albums
    @staticmethod
    def get_albums(client_socket):
        print("Option Get Albums")
        client_socket.send(str(list(data.ALBUMS)).encode('utf-8'))

    # Get all songs in given album
    @staticmethod
    def get_songs_in_album(client_socket):
        client_socket.send("Enter Album Name:\n".encode('utf-8'))
        album = client_socket.recv(1024).decode('utf-8')
        client_socket.send(str(data.ALBUMS[album]).encode('utf-8'))

    # Get Length of given song
    @staticmethod
    def get_song_length(client_socket):
        client_socket.send("Enter Song Name:\n".encode('utf-8'))
        song = client_socket.recv(1024).decode('utf-8')
        d = data.get_song_data(song)[1]
        client_socket.send(str(d[1]).encode('utf-8'))

    # Get Lyrics of given song
    @staticmethod
    def get_song_lyrics(client_socket):
        client_socket.send("Enter Song Name:\n".encode('utf-8'))
        song = client_socket.recv(1024).decode('utf-8')
        client_socket.send(str(data.get_song_data(song)[1][2]).encode('utf-8'))

    # Get album of given song
    @staticmethod
    def get_album_from_song(client_socket):
        client_socket.send("Enter Song Name:\n".encode('utf-8'))
        song = client_socket.recv(1024).decode('utf-8')
        client_socket.send(str(data.get_song_data(song)[0]).encode('utf-8'))

    # Get all song titles that include given phrase
    @staticmethod
    def get_titles_from_word(client_socket):
        client_socket.send("Enter Word:\n".encode('utf-8'))
        word = client_socket.recv(1024).decode('utf-8')
        client_socket.send(str(data.get_songs_from_word(word)).encode('utf-8'))

    # Get all songs that include given lyric
    @staticmethod
    def get_songs_from_lyric(client_socket):
        client_socket.send("Enter Lyric:\n".encode('utf-8'))
        lyric = client_socket.recv(1024).decode('utf-8')
        client_socket.send(str(data.get_songs_from_lyric(lyric)).encode('utf-8'))

    # Function dictionary
    functions = {
        "1": get_albums,
        "2": get_songs_in_album,
        "3": get_song_length,
        "4": get_song_lyrics,
        "5": get_album_from_song,
        "6": get_titles_from_word,
        "7": get_songs_from_lyric
    }


if __name__ == "__main__":
    server = Server()
    server.open_server()

