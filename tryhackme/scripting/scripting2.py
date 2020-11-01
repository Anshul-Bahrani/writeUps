import sockets

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect("10.10.222.145", 3010)