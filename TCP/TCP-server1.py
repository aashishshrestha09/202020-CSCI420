'''
Name: Paul Talaga
Date: 2-25-2020
Desc: TCP server able to handle one client at a time.

'''

import socket

port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind( ('127.0.0.1', port) )
s.listen()

while True:
  print("Waiting for accept")
  client_socket, addr = s.accept()
  with client_socket:
    print("Got connect from {}".format(addr))
    while True:
      msg = client_socket.recv(1024) 
      if not msg:  # msg is None  False
        print("Client disconnect")
        break
      print("Got: {}".format(msg))
      msg = msg.decode('ascii') + " haha!"
      client_socket.sendall(msg.encode('ascii'))