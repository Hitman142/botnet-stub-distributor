
import socket               


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
host = socket.gethostname()
TCP_IP = '127.0.0.1'
ip = socket.gethostbyname(socket.gethostname())
port = 22              
s.bind((TCP_IP, port))        
print(host)
print(ip)
s.listen(5)
f = open("memes.bat",'wb')
while True:
   c, addr = s.accept()     
   print ("Got connection from", addr)
   c.send("You are in")

   while (True):       
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
   f.close()


   c.close()

   s.close()       
