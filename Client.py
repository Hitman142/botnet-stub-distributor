import socket
from time import sleep
s = socket.socket()

host = socket.gethostname()

port = 1234

s.connect((host, port))
print("-->")
i = input()
print("Sending data")
s.sendall(bytes(i, 'utf-8'))
print(s.recv(1024))
print("Done sending")
