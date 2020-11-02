import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
	try:
		s.connect(("10.10.113.180", 1337))
		s.send("GET / HTTP/1.0\r\n\r\n".encode())
		print(s.recv(4096).decode())
	except ConnectionRefusedError:
		continue
	# print(s.recv(4096).decode())