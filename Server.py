import socket, winsound, os, shutil

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostbyname(socket.gethostname())
print("▓█████▄ ▓█████ ▓█████  ██▓███   ███▄    █ ▓█████▄▄▄█████▓")
print("▒██▀ ██▌▓█   ▀ ▓█   ▀ ▓██░  ██▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒")
print("░██   █▌▒███   ▒███   ▓██░ ██▓▒▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░")
print("░▓█▄   ▌▒▓█  ▄ ▒▓█  ▄ ▒██▄█▓▒ ▒▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░") 
print("░▒████▓ ░▒████▒░▒████▒▒██▒ ░  ░▒██░   ▓██░░▒████▒ ▒██▒ ░") 
print("▒▒▓  ▒ ░░ ▒░ ░░░ ▒░ ░▒▓▒░ ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░")   
print("░ ▒  ▒  ░ ░  ░ ░ ░  ░░▒ ░     ░ ░░   ░ ▒░ ░ ░  ░   ░")
print(host)
port = 3467
port2 = 3469
o = "10.217.19.33"
p = "10.217.19.32"
ip = "10.217.19.34"
s.bind((host, port))
s.listen(50)

def receive():
    c, addr = s.accept()
    print('Got connection from', addr)
    a = c.recv(5000)
    print('Received message == ',a)
    
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((o, port2))
    v = input("Type in response")
    s2.send(bytes(str(v), 'utf-8'))
    if bytes("close", 'utf-8') in a:
       winsound.PlaySound("roblox.wav", winsound.SND_FILENAME)
       s.close()
       
      
    if bytes("read", 'utf-8') in a:
       address = 'C:\\Program Files (x86)\\Steam\\skins\\skins_readme.txt'
       f = open(address,'rb')  
       data = f.read()

       s2.send(bytes(str(data), 'utf-8'))
       print("File text received")
       f.close()
    if bytes("delete", 'utf-8') in a:
       os.remove("C:/Users/iD Student/Desktop/GRAHAM B/abc/abcd.txt")
       print("Text file deleted")

    if bytes("dels", 'utf-8') in a:
        shutil.rmtree("C:/Users/iD Student/Documents/deleteee")
        print("File deleted")
       
       
    else:
        a2 = c.recv(500)
        print('Received message == ',a2)
        v = input("Type in response")
        s2.send(bytes(str(v), 'utf-8'))
       
    while True:
        
        a3 = c.recv(500)
        print('Received message == ',a2)
        v = input("Type in response")
        s2.send(bytes(str(v), 'utf-8'))
             
while True:
   receive()
   
