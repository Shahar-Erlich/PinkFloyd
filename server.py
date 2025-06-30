import socket
import data #import the txt parser
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)

#Function that handles client/user inputs
def handleClient():
    #While server is running
    while True:
        #Data sent from user
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break;
        #if code is 8, disconnect  client socket
        if data == '8':
            client_socket.close()
        else:
            #call the function handle stored in the dictionary
            functions[data]()
        print("from connected user: " + str(data))

#Get all albums
def getAlbums():
    print("Option Get Albums")
    client_socket.send(str(list(data.getAlbums())).encode('utf-8'))

#Get all songs in given album
def getSongsInAlbum():
    client_socket.send("Enter Album Name:\n".encode('utf-8'))
    Album = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getAlbums()[Album]).encode('utf-8'))

#Get Length of given song
def getSongLength():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    d = data.getSongData(Song)[1]
    client_socket.send(str(d[1]).encode('utf-8'))

#Get Lyrics of given song
def getSongLyrics():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongData(Song)[1][2]).encode('utf-8'))

#Get album of given song
def getAlbumFromSong():
    client_socket.send("Enter Song Name:\n".encode('utf-8'))
    Song = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongData(Song)[0]).encode('utf-8'))

#Get all song titles that include given phrase
def getTitlesFromWord():
    client_socket.send("Enter Word:\n".encode('utf-8'))
    Word = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongsFromWord(Word)).encode('utf-8'))

#Get all songs that include given lyric
def getSongsFromLyric():
    client_socket.send("Enter Lyric:\n".encode('utf-8'))
    Lyric = client_socket.recv(1024).decode('utf-8')
    client_socket.send(str(data.getSongsFromLyric(Lyric)).encode('utf-8'))

#Function dictionary
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
    #Parse the text file to structs
    data.createDataBase()
    #bind server to address/port
    server_socket.bind(CONNECTION)
    #listen to client connections
    server_socket.listen()
    #wait to accept clients trying to connect
    (client_socket, client_address) = server_socket.accept()

    print("Client Connected!")
    #send welcome message to client
    client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
    #handle client
    handleClient()

