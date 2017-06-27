
import socket               


s = socket.socket()         
host = socket.gethostname()
TCP_IP = '127.0.0.1'
ip = socket.gethostbyname(socket.gethostname())
port = 22              
s.bind((TCP_IP, port))        
print(host)
print(ip)

s.listen(1)
c, addr = s.accept()

print ("Got connection from" + str(addr))
while True:
   s = c.recv(1024).decode()
   if not data:
      break
   print("from connected user: " + str(s))
   s = str(s).upper()
   print("sending: " + str(s))
   c.send(s.encode())

print("Done Recieving")
c.send("Thank you for connecting")  
c.close()
