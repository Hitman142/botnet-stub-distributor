import socket, winsound

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print("▓█████▄ ▓█████ ▓█████  ██▓███   ███▄    █ ▓█████▄▄▄█████▓")
print("▒██▀ ██▌▓█   ▀ ▓█   ▀ ▓██░  ██▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒")
print("░██   █▌▒███   ▒███   ▓██░ ██▓▒▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░")
print("░▓█▄   ▌▒▓█  ▄ ▒▓█  ▄ ▒██▄█▓▒ ▒▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░") 
print("░▒████▓ ░▒████▒░▒████▒▒██▒ ░  ░▒██░   ▓██░░▒████▒ ▒██▒ ░") 
print("▒▒▓  ▒ ░░ ▒░ ░░░ ▒░ ░▒▓▒░ ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░")   
print("░ ▒  ▒  ░ ░  ░ ░ ░  ░░▒ ░     ░ ░░   ░ ▒░ ░ ░  ░   ░")
print(host)
port = 1234
port2 = 12345
o = "10.217.19.33"
ip = "10.217.19.34"
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    a = c.recv(50)
    print('Received message == ',a)
    s2.connect((o, port2))
    if bytes("close", 'utf-8') in a:
       winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
       s.close()
       break
    if bytes("read", 'utf-8') in a:
       f = open('skins_readme.txt','rb')  
       data = f.read()
       print(data)
       s2.send(bytes(str(data), 'utf-8'))
    else:
       f.close()
       c.send(a)
       c.close()
