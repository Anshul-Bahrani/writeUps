import urllib.request
for i in range(0,99):
	page = urllib.request.urlopen('http://10.10.150.221/th1s_1s_h1dd3n/?secret=' + str(i))
	if 'That is wrong' not in page.read().decode('utf_8'):
		print(i)