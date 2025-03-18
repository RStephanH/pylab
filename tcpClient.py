import socket
target_host=""
target_port=""
target_host=str(input("Enter your target host : "))
target_port=str(input("Enter your port target : "))

#Let's create a socket object 
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client
client.connect((target_host,target_port))

#Send some data
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

#receive some data
response=client.recv(4096)

print(response.decode())
client.close()
