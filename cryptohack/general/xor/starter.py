#!/usr/bin/env python3

s = "label"

finalAnswer = []
for elem in s:
	finalAnswer.append(chr(ord(elem)^13))

print("".join(finalAnswer))