import os

words = open("random.dic", "r")
print(words)
os.system("pwd")
for elem in words.readlines():
	elem = elem[:len(elem) - 1]
	print(elem)
	os.system("./program " + elem)