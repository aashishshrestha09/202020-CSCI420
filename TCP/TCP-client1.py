'''
Name: Paul Talaga
Date: 2-25-2020
Desc: TCP client with a send/receive loop.

'''
import socket

port = 5556 #  Send to port above 1024

host = socket.gethostname()
#host = '10.18.101.97'
host = '127.0.0.1'
print("I am {}".format(host))

# the width releases the resouces when you ctrl-c
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect( (host, port))
  while True:
    message = input("What do you want to send?")
      #s.send( message.encode('ascii'))
    if message == 'exit':
      break
    s.sendall( message.encode('ascii'))
    print("Message Sent!")
    rcv = s.recv(1024)
    print("Got: {}".format(rcv.decode('ascii')))
  s.close()