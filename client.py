import socket

"""
199 => ask to connect
200 => OK connect, followed by token after space
400 => Bad request
401 => KO connect, bad token
405 => KO method not allowed
409 => KO conflict token
500 => KO Internal Serveur Error
"""


class TCPClient:
    "TCP client"

    def __init__(self):
        #WIP : GUI change it
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server

    def send(self,msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(msg)
            data = s.recv(1024)
        print('Received', repr(data))

    def connect(self):
        self.send(b'199')





clt = TCPClient()
clt.connect()
