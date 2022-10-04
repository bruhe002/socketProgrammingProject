import socket 

import sys


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PREPARE A SERVER SOCKET

serverPort = 4189
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Ready to serve...')

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n" % filename)

        # # Send content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        pass
        # Send Response message for file not found
        connectionSocket.send("HTTP/1.1 404 ")
        # Close client socket
        # Fill in start
        # Fill in end

    # serverSocket.close()
    # sys.exit() # Terminate the program after sending the corresponding data 
