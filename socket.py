from socket import *

import sys


serverSocket = socket(AF_INET, SOCK_STREAM)

# PREPARE A SERVER SOCKET

serverPort = 4189
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Ready to serve...')

while True:
    # Establish the connection
    # print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # outputdata = # Fill in start # Fill in end
        # Send one HTTP header line into socket
        # Fill in Start 
        # Fill in end
        # 
        # # Send content of the requested file to the client
        # for i in range(0, len(outputdata)):
        #   connectionSocket.send(outputdata[i].encode())
        # connectionSocket.send("\r\n".encode())
        # 
        # 
        # 
        # connectionSocket.close()
        pass
    except IOError:
        pass
        # Send Response message for file not found
        # Fill in start
        # Fill in End
        # Close client socket
        # Fill in start
        # Fill in end

    # serverSocket.close()
    # sys.exit() # Terminate the program after sending the corresponding data 
