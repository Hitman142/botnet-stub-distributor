
import socket               


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
host = socket.gethostname()
TCP_IP = '10.217.19.33'
port = 80              
s.bind((TCP_IP, port))        
print(host)
s.listen(5)                 
while True:
   c, addr = s.accept()     
   print ("Got connection from", addr)
   c.send("Thank you for connecting")
   c.close()       
