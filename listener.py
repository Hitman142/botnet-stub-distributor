import socket, winsound
from time import sleep

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
host2 = "0.0.0.0"
print(host)
port = 3467
port2 = 3469

s2.bind((host, port2))
s2.listen(50)

while True:
    c2, addr = s2.accept()
    print('Got connection from', addr)
    a2 = c2.recv(4096)
    print('Received message == ', a2)
    s2.close

    
       


