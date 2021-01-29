import socket
import random


class TCPServer:
    "TCP server"
    
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server
        self.TOKENS = []

    def newToken(self):
        pass

    def start(self):
                
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((self.HOST, self.PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        if data == b'199':
                            #give a token
                            data += b'200 '

                        conn.sendall(data)
                        

srv = TCPServer()
srv.start()
