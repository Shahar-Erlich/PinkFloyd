import socket
import data #import the txt parser
import hashlib
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)
HASH_PASS = "0c9420a304a2267b42962a958c95609d" #Bashed Password
#Function that handles client/user inputs
#check if user is still connected
connected = True
def handleClient():
    #While server is running
    global connected
    while True:
        #Data sent from user
        if connected:
          data = client_socket.recv(1024).decode('utf-8')
          if not data:
                break;
          #if code is 8, disconnect  client socket
          if data == '8':
               client_socket.close()
               connected = False
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

    #send password message to client
    client_socket.send(f'Enter Password'.encode('utf-8'))
    #loop and check each time if the client sent the correct password
    while hashlib.md5(client_socket.recv(1024)).hexdigest() != HASH_PASS:
        client_socket.send(f'Enter Password'.encode('utf-8'))

    print("Client Connected!")
    connected = True
    #send welcome message to client
    client_socket.send(f'Correct!'.encode('utf-8'))
    client_socket.send(f'Welcome {client_address}'.encode('utf-8'))
    #handle client
    handleClient()

