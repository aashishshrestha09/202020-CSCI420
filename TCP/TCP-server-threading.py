'''
Name: Aashish Shrestha
Date: 3-10-2021
Desc: TCP server to distributed message to all clients connected
'''

import socket
import threading


def TCPworker(sockets):
    client_socket, addr = sockets[-1]
    print(addr)
    print("There are {} things in socket_list.".format(len(socket_list)))
    while True:
        try:
            msg = client_socket.recv(1024)
            # if not msg:
            #     print("Client disconnect")
            #     break
        except:
            print("Client disconnect")
            break
        print("Got: {}".format(msg))
        msg = msg.decode('ascii')
        for other_soc, other_addr in sockets:
            if (client_socket, addr) != (other_soc, other_addr):
                print("Sending to {}".format(other_addr))
                other_soc.sendall(msg.encode('ascii'))
    sockets.remove((client_socket, addr))


port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_list = []

s.bind(('127.0.0.1', port))
s.listen()

while True:
    print("Waiting for accept")
    client_socket, addr = s.accept()
    socket_list.append((client_socket, addr))
    print("Adding {} to socket list".format(addr))
    thread = threading.Thread(target=TCPworker, args=[socket_list])
    thread.start()

