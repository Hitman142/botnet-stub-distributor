import socket, winsound
from time import sleep


def connect():
    print(".______  ._______._______._______ .______  .____________._")
print("    :_ _   \ : .____/: .____/: ____  |:      \ : .____/\__ _:|")
print("    |   |   || : _/\ | : _/\ |    :  ||       || : _/\   |  :|")
print("    | . |   ||   /  \|   /  \|   |___||   |   ||   /  \  |   |")
print("    |. ____/ |_.: __/|_.: __/|___|    |___|   ||_.: __/  |   |")
print("    :/         :/      :/                |___|   :/     |___|")
print("    :                                                        ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
o = "10.217.19.33"
print(host)
ip = "10.217.19.34"
port = 3467
port2 = 3469

s.connect((o, port))
while 1:
    msg = input("Command To Send: ") 
    s.send(bytes(msg, 'utf-8'))
    if "close" in msg:
        winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
   

while True:
    connect()
    s.close
