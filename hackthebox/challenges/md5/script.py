import os
import requests
import hashlib

content = requests.get("http://docker.hackthebox.eu:30804/")

post = content.text

# posi = get.find("<h3 align='center'>")

# posi2 = get.find("</h3>")

# print(get, posi, posi2, get[167:187])

# os.system("echo ")
# for i in range()
# op = os.system("echo '" + get[167:187] + "' | md5sum")
for i in range(200):

	res = hashlib.md5(post[167:187].encode())

	# print(res.hexdigest())
	data = {'hash' : res.hexdigest()}
	# print(data)

	post = requests.post("http://docker.hackthebox.eu:30804/", data = data).text
	if "Too slow!" not in post:
		print(post)
		break
