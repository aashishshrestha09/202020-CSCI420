"""
UDP-Server.py
Paul Talaga
Feb 7, 2020
Desc: Lab 4 chat server.

"""
import socket

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1200

def getConversations(convos, person):
  ret = "{} Users\n".format(len(conversations.keys()))
  for p in convos.keys():
    ret += "{}: {}\n".format(convos[p]['name'], convos[p]['message'])
  return ret

print("Server Started.  Listening...")

conversations = {}

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.bind(  (serverIP,serverPort) )
    
    while True:
        (newMessage, clientAddress) = server.recvfrom(2048)
        print("Got: {} from {}".format(newMessage, clientAddress))

        newMessage = newMessage.decode('utf-8')

        if clientAddress not in conversations.keys():
            conversations[clientAddress] = {'name': "User-" + str(len(conversations)), 
                                            'message': "--"}

        if newMessage[0:5] == 'Name:':
          conversations[clientAddress]['name'] = newMessage[5:]
          print("Name change: {}".format(newMessage[5:]))
        elif newMessage != '.':
          conversations[clientAddress]['message'] = newMessage
        

        newMessage = getConversations(conversations, clientAddress)
        
        server.sendto(newMessage.encode('utf-8'), clientAddress)
    
    server.close()
    