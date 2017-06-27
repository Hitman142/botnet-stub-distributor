import socket, winsound
from time import sleep

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port2 = 12345

s2.bind((host, port2))
s2.listen(5)

while True:
    c2, addr = s2.accept()
    print('Got connection from', addr)
    a = c2.recv(4096)
    print('Received message == ',a)



    c2.send(a)
    c2.close()
    
       


