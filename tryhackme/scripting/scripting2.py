import socket
import sys
import time

ip = "10.10.41.184"
port = 1337
answer = 0.00000

def operation(operator, number):
	global answer
	print(f"{answer} {operator} {number}")
	if operator == "add":
		answer += number
	elif operator == "minus":
		answer -= number
	elif operator == "divide":
		answer /= number
	elif operator == "multiply":
		answer *= number
	else:
		print("STOP Found: ",operator)
		print("Final answer: ", answer)
		sys.exit(0)
while port != 9765:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		time.sleep(1)
		s.connect((ip, port))
		s.send(f"GET / HTTP/1.0\r\n\r\nHost: {ip}:{port}\r\n\r\n".encode())
		print(f"\nFound {port}: ")
		fullContent = s.recv(4096).decode()
		# print(fullContent)
		lineSplitted = [x for x in fullContent.split("\n")]
		print(len(lineSplitted))
		if len(lineSplitted) <= 3:
			continue
		mainContent = lineSplitted[6]
		print("Main:", mainContent)
		operator, number, port = mainContent.split()
		port = int(port)
		operation(operator,float(number))
		s.close()
	except ConnectionRefusedError:
		print(f"Trying {port}...",end="\r")
		continue
print("\nPort 9765 found final answer: ", answer)
	# print(s.recv(4096).decode()) Host: {ip}:{port}

# Port 9765 found final answer:  344769.12000000005