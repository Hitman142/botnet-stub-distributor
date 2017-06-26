import socket, sys


def bots():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_IP = '128.42.52.243'
    host = socket.gethostname()
    port = 22

    s.connect((TCP_IP, port))
    f = open ("memes.bat", "rb")
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
        
        s.send("memes/adgbkilern;ogn;tsr")
        s.close
bots()
