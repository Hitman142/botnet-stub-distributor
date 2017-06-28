import os


hostname = input ("Type in your target: ")
response = os.system("ping -n 1" + hostname)

if response == 0:
    print(hostname, 'is offline')
else:
    print(hostname, 'is online')
