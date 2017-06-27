import socket, winsound

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(host)
port = 1234

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    a = c.recv(50)
    str(a, 'utf-8')
    #a = a.strip(bytes('\'', 'utf-8'))
    a.strip(bytes('b', 'utf-8'))
    print('Received message == ',a)

    if bytes("greedy", 'utf-8') in a:
       take all files()
    if bytes("close", 'utf-8') in a:
       winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
       s.close()
       break
    else:
       c.send(a)
       c.close()
