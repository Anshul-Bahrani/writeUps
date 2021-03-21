#!/usr/bin/env python3

p = 17
q = 23
e = 65537
N = p*q
print(N)
print((12**e)%N)