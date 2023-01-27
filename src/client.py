"""

Author: Anders Mouanga (salticecream)
Description: Client software for the IMSigma (Instant Messaging Sigma) application.


Note: Some code is kindly borrowed from https://www.geeksforgeeks.org/socket-programming-python/ where
appropriate.

"""

import socket
import sys
from threading import Thread

HOST = "127.0.0.1"
PORT = 2625
MAX_MESSAGE_LENGTH = 255

s = socket.socket()

s.connect( (HOST, PORT) )

""" damn i hate windows. of course select.select() doesn't work on this useless OS """


# send messages
def send_messages(_socket=s):
    while True:
        message_sent = sys.stdin.readline()
        _socket.send(message_sent.encode())
        sys.stdout.write(f"[You]: {message_sent}")
        sys.stdout.flush()

# read messages
def read_messages(_socket=s):
    while True:
        message_received = _socket.recv(MAX_MESSAGE_LENGTH).decode()
        if message_received:
            print(message_received)

def main():

    send = Thread(target = send_messages, args = (s,) )
    read = Thread(target = read_messages, args = (s,) )

    send.start()
    read.start()
    send.join()
    read.join()

main()
