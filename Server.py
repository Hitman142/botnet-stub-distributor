
import socket               


s = socket.socket()         
host = socket.gethostname()
TCP_IP = '127.0.0.1'
ip = socket.gethostbyname(socket.gethostname())
port = 22              
s.bind((TCP_IP, port))        
print(host)
print(ip)
s.listen(5)
f = open("memes.txt",'wb')
c, addr = s.accept()
s.close
print ("Got connection from", addr)
print("Receiving")
while True:
   data = c.recv(1024).decode()
   if not data:
      break
   print("from connected user: " + str(data))
   data = str(data).upper()
   print("sending: " + str(data))
   c.send(data.encode())
c.close()
print("Done Recieving")
c.send("Thank you for connecting")  

c.close()
       
