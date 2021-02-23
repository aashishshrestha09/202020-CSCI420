"""
UDP-Client.py
Paul Talaga
Feb 7, 2020
Desc: Lab 4 chat client.

"""
import socket
import threading

serverIP = 'localhost'
serverPort = 1200

clientSocket = None

def printIncoming():
  while clientSocket:
    (newMessage, serverAddress) = clientSocket.recvfrom(2048)
    print(newMessage.decode('utf-8'))


if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set up listener
    listener = threading.Thread(target=printIncoming)
    listener.start()
    
    while True:
        message = input("Enter a message:")
        clientSocket.sendto(message.encode('utf-8'), (serverIP,serverPort))
        
    clientSocket.close()
    clientSocket = None
    listener.join()
    
  