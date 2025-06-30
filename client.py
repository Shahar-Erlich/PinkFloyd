import socket
ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)

#create client socket
client_socket = socket.socket()
#connect to server address/port
client_socket.connect(CONNECTION)
#recieve welcome message and print
data = client_socket.recv(1024).decode('utf-8')
print(data)

Instruction = ("1.ListAlbums - List all albums\n"
               "2.ListSongs (Album name) - List all songs in given album\n"
               "3.Length (Song name) - Get length of given song\n"
               "4.Lyrics (Song name) - Get lyrics of given song\n"
               "5.GetAlbum (Song name) - Get the album of given song\n"
               "6.GetSongTitle (Word) - Get all song names that include given word\n"
               "7.GetSongLyric (Lyric) - Get all songs with given word in lyrics\n"
               "8.Exit - Exit client")
#print instructions
print(Instruction)
option = ""
#loop the client until exit code is inputted
while(option != "8"):
    option = input("Enter option\n")
    client_socket.send(option.encode('utf-8'))
    #if no extra info needed get answer instantly
    if(option == "1"):
        print(client_socket.recv(1024).decode('utf-8'))
    #if extra info needed after choosing (song name/album name) send the extra info and recieve final info
    else:
        print(client_socket.recv(1024).decode('utf-8'))
        inp = input()
        client_socket.send(inp.encode('utf-8'))
        print(client_socket.recv(1024).decode('utf-8'))

