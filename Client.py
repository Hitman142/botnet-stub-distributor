import socket, winsound
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
host2 = "y700-PF0FQPAW"
host3 = "y700-PF0FVLBY"
o = "10.217.19.33"
print(host)
ip = "10.217.19.34"
port = 1234

s.connect((o, port))
while 1:
    msg = input("Command To Send: ") 
    s.send(bytes(msg, 'utf-8'))
    if "close" in msg:
       winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
       


