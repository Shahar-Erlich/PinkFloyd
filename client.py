import socket
ADDR = '127.0.0.1'
PORT = 8820
CONNECTION = (ADDR, PORT)
APPROVE_MESSAGE = "Correct!"

class Client:

    def __init__(self):
        '''
        initializes the client with a socket
        '''
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client_socket.setblocking(False)
    def print_options(self):
        '''
        Method that prints the instructions to the user
        '''
        Instruction = ("1.ListAlbums - List all albums\n"
                       "2.ListSongs (Album name) - List all songs in given album\n"
                       "3.Length (Song name) - Get length of given song\n"
                       "4.Lyrics (Song name) - Get lyrics of given song\n"
                       "5.GetAlbum (Song name) - Get the album of given song\n"
                       "6.GetSongTitle (Word) - Get all song names that include given word\n"
                       "7.GetSongLyric (Lyric) - Get all songs with given word in lyrics\n"
                       "8.Exit - Exit client")
        print(Instruction)

    def try_connect_server(self):
        '''
        Method that tries to connect to the server
        Will not let the user through untill a correct password is entered
        After which it will let the user connect and use the server
        '''
        self.client_socket.connect(CONNECTION)
        data = client.client_socket.recv(1024).decode('utf-8')
        while data != APPROVE_MESSAGE:
            password = input("Enter password:\n")
            self.client_socket.send(password.encode('utf-8'))
            data = self.client_socket.recv(1024).decode('utf-8')
        print(data)
        data = self.client_socket.recv(1024).decode('utf-8')
        print(data)
        self.use_server()

    def use_server(self):
        '''
        Method that waits for user input,
        sends it to the server and accepts the answer
        '''
        self.print_options()
        option = ""
        while (option != "8"):
            option = input("Enter option\n")
            self.client_socket.send(option.encode('utf-8'))
            if (option == "1"):
                print(self.client_socket.recv(1024).decode('utf-8').replace('\'',""))
            elif option != "8":
                print(self.client_socket.recv(1024).decode('utf-8'))
                inp = input()
                self.client_socket.send(inp.encode('utf-8'))
                print(self.client_socket.recv(1024).decode('utf-8'))


if __name__ == '__main__':
    client = Client()
    client.try_connect_server()


