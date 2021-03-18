#!/usr/bin/env python3

from pwn import xor

r = open("lemur.png", "rb")

img1 = bytearray(r.read())
r.close()
#print(img1)
pngHeader = img1[:8]

for ind in range(8):
	print(img1[ind])

img1 = img1[8:]
print(len(img1))

potentialKey = "crypto"




print("---------------")
t = open("test.png", "rb")
txt = bytearray(t.read())
t.close()
for elem in range(8):
	print(txt[elem])

img2 = open("flag.png", "rb")

flag_txt = bytearray(img2.read())

print(len(flag_txt))

towrite = xor(img1, flag_txt)

toWrite = open("test.png", "wb")
temp = pngHeader + towrite
print("Temp:", len(temp), temp[:8])
toWrite.write(pngHeader)
toWrite.write(temp)
toWrite.close()