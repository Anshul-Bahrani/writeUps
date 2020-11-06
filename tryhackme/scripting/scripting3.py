import socket

ip = "10.10.33.48"

port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	s.connect((ip, port))
	message = input()
	s.send(message.encode())
	print(s.recv(4096).decode())