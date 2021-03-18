#!/usr/bin/env python3

import base64
import codecs

print(base64.b64encode("Hi".encode()).decode())

print(base64.b64decode("SGk=".encode()).decode())

print(codecs.getencoder("rot-13")("uryyb")[0])

print("abcdef", end="\r")

while(True):
	print("[~] Sending", end="\r")