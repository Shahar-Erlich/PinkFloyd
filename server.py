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
        else:
            functions[data]()
        print("from connected user: " + str(data))

def getAlbums():
    print("Option Get Albums")
    client_socket.send(str(list(data.getAlbums())).encode('utf-8'))

def getSongsInAlbum():
    client_socket.send("Enter Album Name:\n".encode('utf-8'))
    Album = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getAlbums()[Album]).encode('utf-8'))

def getSongLength():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    d = data.getSongData(Song)[1]
    client_socket.send(str(d[1]).encode('utf-8'))

def getSongLyrics():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongData(Song)[1][2]).encode('utf-8'))

def getAlbumFromSong():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongData(Song)[0]).encode('utf-8'))

def getTitlesFromWord():
    client_socket.send("Enter Word:\n".encode('utf-8'))
    Word = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongsFromWord(Word)).encode('utf-8'))

def getSongsFromLyric():
    client_socket.send("Enter Lyric:\n".encode('utf-8'))
    Lyric = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongsFromLyric(Lyric)).encode('utf-8'))

functions = {
    "1" : getAlbums,
    "2" : getSongsInAlbum,
    "3" : getSongLength,
    "4" : getSongLyrics,
    "5" : getAlbumFromSong,
    "6" : getTitlesFromWord,
    "7" : getSongsFromLyric
}


if __name__ == "__main__":
    data.createDataBase()
    server_socket.bind(CONNECTION)
    server_socket.listen()
    (client_socket, client_address) = server_socket.accept()

    print("Client Connected!")
    client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
    handleClient()

