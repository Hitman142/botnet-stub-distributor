import socket, sys


def connect():
    s = socket.socket()
    TCP_IP = '128.42.52.243'
    host = socket.gethostname()
    port = 22

    s.connect((TCP_IP, port))
    message = input(" -> ")
    s.send(b"I Am Connecting")
    f = open("memes.txt", "rb")
  
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input(" -> ")
    s.close
    f.close
    print("Done") 
connect()
