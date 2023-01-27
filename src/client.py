"""

Author: Anders Mouanga (salticecream)
Description: Client software for the IMSigma (Instant Messaging Sigma) application.


Note: Some code is kindly borrowed from https://www.geeksforgeeks.org/socket-programming-python/ where
appropriate.

"""

import socket
import select
import sys

HOST = "127.0.0.1"
PORT = 2625
MAX_MESSAGE_LENGTH = 255

running = True

s = socket.socket()

s.connect( (HOST, PORT) )


while True:

    list_of_sockets = [socket.socket(), s]
    read_sockets, write_socket, error_socket = select.select(list_of_sockets, [], [])

    # Read messages
    for _socket in read_sockets:
        if _socket == s:
            message_received = s.recv(MAX_MESSAGE_LENGTH).decode()
            print(message_received)
        else:
    # Send messages
            message_sent = sys.stdin.readline()
            s.send(message_sent.encode())
            sys.stdout.flush()

    



print(
    s.recv(1024).decode()
)

s.close()



