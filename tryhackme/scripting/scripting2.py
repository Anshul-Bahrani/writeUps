import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "10.10.70.49"
port = 3010
while True:
	try:
		s.connect((ip, port))
		s.send(f"GET / HTTP/1.0\r\n\r\nHost: {ip}: {port}".encode())
		print(s.recv(4096).decode())
	except ConnectionRefusedError:
		continue
	# print(s.recv(4096).decode())