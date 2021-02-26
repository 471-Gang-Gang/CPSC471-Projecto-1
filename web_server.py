#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

# TASK 1
#Fill in start
serverPort = 45678
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('the web server is up on port:', serverPort)
#Fill in end

while True:
   #Establish the connection
   print('Ready to serve...')
   # TASK 2
   connectionSocket, addr = serverSocket.accept()

   try:
      # TASK 3
      message = connectionSocket.recv(1024)
      print('Message: ', message)  #testing 
      filename = message.split()[1]
      print('Filename: ', filename) #testing filename
      f = open(filename[1:],"r")
      outputdata = f.read()
      # print(outputdata)
      # TASK 5
      #Send one HTTP header line into socket
      #Fill in start
      connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n","UTF-8"))
      #Fill in end

      #Send the content of the requested file to the client
      for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
      connectionSocket.send("\r\n".encode())
      connectionSocket.close()
   except IOError:


      # TASK 6
      #Send response message for file not found
      #Fill in start
      connectionSocket.send(bytes("\nHTTP/1.1 404 Not Found\n\n", "UTF-8"))
      
      #Fill in end

      # TASK 7
      #Close client socket
      #Fill in start
      connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>","UTF-8"))
      connectionSocket.close()
      #Fill in end

serverSocket.close()
sys.exit()   #Terminate the program after sending the corresponding data
