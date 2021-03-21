#!/usr/bin/env python3


def gcd(a ,b):
	# Euclid's Algorithm
	if a == 0:
		return b
	return gcd(b%a, a)
a = 66528 
b = 52920

print(gcd(a, b))