#program to display ip address of your computer
import socket
hostname=(socket.gethostname())
ip=(socket.gethostbyname(hostname))
print (ip)
