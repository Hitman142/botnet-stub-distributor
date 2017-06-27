import socket, winsound
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
host2 = "y700-PF0FQPAW"

port = 1234

s.connect((host2, port))
while 1:
    msg = input("Command To Send: ")
    
       
    s.send(bytes(msg, 'utf-8'))
    if "close" in msg:
       winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
       

#print("-->")
#i = input()
#print("Sending data")
#s.sendall(bytes(i, 'utf-8'))
#print(s.recv(1024))
#print("Done sending")

