import socket

s = socket.socket()

host = socket.gethostname()

port = 1234

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    a = c.recv(50)
    print('Received message == ',a)
    c.send(a)
    c.close()
