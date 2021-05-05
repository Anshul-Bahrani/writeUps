from base64 import b64decode
from base64 import b64encode
import requests
import threading
url = "http://mercury.picoctf.net:15614"
s = requests.session()
s.get(url)
cookie = s.cookies.get_dict()["auth_name"]
# print(cookie)
# cookie = "NmExZDF3clpaenV1T29sd3RSYlcyUHcrWXY1NitqYlFTWUl6QWtwZ1FiRHlFdzlxa3NUNEZBMmk1RS85bEFxMm9XbHczMTBHNnEvVXduLzZQR3BmeUFaNnBkY0trbk9DWTFPUFYycUxCeENOMllKc1B3aXBQN0NRcWx0WGpZbXM="
data = str(b64decode(cookie))
# print(data)
def flip(pos, bit):
	global data
	ls = list(data)
	# print("LS:", ls)
	ls[pos] = chr(ord(ls[pos])^bit)
	return "".join(ls)
def foo(i):
	for tmp in range(10):
		for j in range(128):
			print("[~] Testing for", i, j,"\t\t\t\t\t",end="\r")
			current = b64encode(flip(i, j).encode())
			# print("Current", current.decode())
			cookie = {
				'auth_name': current.decode()
				}
			txt = s.get(url, cookies=cookie).text
			if "picoCTF{" in txt:
				print("Found", txt)
				break
		i += 1
		if i == 128:
			break

for elem in range(0, 130, 10):
	print("Start:", elem)
	t1 = threading.Thread(target=foo, args=(elem,))
	t1.start()