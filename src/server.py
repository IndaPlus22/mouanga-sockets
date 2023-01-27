"""

Author: Anders Mouanga (salticecream)
Description: Server software for the IMSigma (Instant Messaging Sigma) application.


Note: Inspiration for some code is taken from https://www.geeksforgeeks.org/socket-programming-python/
and https://www.geeksforgeeks.org/simple-chat-room-using-python/ where appropriate.

"""


import socket
import _thread

# constants

HOST = "127.0.0.1"
PORT = 2625
NONE_CONNECTION = (None, None)

MAX_CONNECTIONS = 5
MAX_MESSAGE_LENGTH = 255


connections = []

# send a message to the client
def send_message(connection, message, silent = False):
    connection.send(message.encode())
    if silent != True:
        print(f"Sent `{message}` to connection `{connection}`")

# send a message to all clients, except the specified one
def send_all_except(connection, message, silent = 2):

    # the "connections" list looks like this: [(connection0, address0), (connection1, address1), ...]
    # so we want to access connection0, connection1, etc
    for connection_tuple in connections:
        if connection_tuple[0] != connection:
            send_message(connection_tuple[0], message, True)

    if silent == 0:
        print(f"Sent `{message}` to: {connections}")
    elif silent == 1:
        print(f"Sent `{message}`")


def thread_loop(connection, address):
    while True:
        # we use try and except here, because we don't want the client to close because of random exceptions
        try:
            message = connection.recv(MAX_MESSAGE_LENGTH).decode()
            # we don't want to print empty messages, thus the "if"
            if message:
                print(f"[{address}]: {message} ")
                send_all_except(connection, f"[{address}]: {message}")
        except BaseException as err:
            # we silently ignore the exception, because otherwise the server console is flooded when somebody leaves
            continue


            




def main():
    running = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    


    # since this is a command line program (for now) and such print statements are common in
    # these types of applications, i decide to not omit these print statements
    print("Successfully created socket...")

    s.bind( (HOST, PORT) )
    print(f"Socket bound to {HOST}:{PORT}...")

    s.listen(MAX_CONNECTIONS)
    print("Socket now listening...")

    while running:
        # wait for a connection, then...
        connection, address = s.accept()
        connections.append( (connection, address) )

        print(f"{address} just connected!")
        send_all_except(connection, f">> {address} << just joined the room!")
        send_message(connection, "Connected", False)
        _thread.start_new_thread(
            thread_loop,
            (connection, address)
        )
    for connection_tuple in connections:
        connection_tuple[0].close()
    

main()