#!/usr/bin/env python3

key = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

#print(key)

#print(b'0')

for elem in range(256):
	toPrint = []
	for elem1 in key:
		toPrint.append(chr(elem ^ elem1))
	toFind = str("".join(toPrint))
	if 'crypto' in toFind:
		print(toFind)