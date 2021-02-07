"""
UDP-SErver.py
Paul Talaga
Feb 7, 2020
Desc: UDP Client/Server Demo

"""
import socket

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1200

print("Server Started.  Listening...")

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.bind(  (serverIP,serverPort) )
    while True:
        (newMessage, clientAddress) = server.recvfrom(2048)
        print("Got: {}".format(newMessage))
        
        newMessage = str(newMessage).upper()
        
        server.sendto(newMessage.encode('utf-8'), clientAddress)
    
    server.close()
    