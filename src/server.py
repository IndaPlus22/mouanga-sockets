"""

Author: Anders Mouanga (salticecream)
Description: Server software for the IMSigma (Instant Messaging Sigma) application.


Note: Some code is kindly borrowed from https://www.geeksforgeeks.org/socket-programming-python/ where
appropriate.

"""


import socket

# constants

HOST = "127.0.0.1"
PORT = 2625

MAX_CONNECTIONS = 5
MAX_MESSAGE_LENGTH = 255
MAX_MESSAGES = 5
MAX_MESSAGES_PERIOD = 10 # seconds

def send_message(connection, message, silent = False):
    connection.send(message.encode())
    if silent != True:
        print(f"Sent `{message}` to connection `{connection}`")



def main():
    running = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # since this is a command line program (for now) and such print statements are common in
    # these types of applications, i decide to not omit these print statements
    print("Successfully created socket...")

    s.bind( ("", PORT) )
    print(f"Socket bound to {PORT}...")

    s.listen()
    print("Socket now listening...")

    while running:
        # wait for a connection, then...
        connection, address = s.accept()

        send_message(connection, "Hello from the server!", False)

        # we try to only send one message..

        connection.close()

        running = False
    

main()





















"""
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully created socket!")
    host_ip = socket.gethostbyname("google.com")
    print(f"Successfully resolved google ip: {host_ip}")
    s.connect((host_ip, 80))
    print("Successfully connected to google!")
except socket.error as err:
    print(f"Error: `{err}`")
finally:
    print("Program done")
"""



