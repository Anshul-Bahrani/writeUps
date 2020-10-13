import requests

url = 'http://10.10.223.170/map.php'

text = 'Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv'

# print(ord(text[0]))
for i in range(26):
	temp = []
	temp.append(chr((ord(text[0]) - 65 + i)%26 + 65))
	for elem in text[1:]:
		if elem != '_':
			elem = chr((ord(elem) - 97 + i)%26 + 97)
		temp.append(elem)
	temp_text = "".join(temp)
	# print(temp_text)
	data = {
		'keycheck' : temp_text
	}
	final = requests.post(url, data = data)
	if "Invaild Key !!!" not in final.text:
		print(temp_text)
