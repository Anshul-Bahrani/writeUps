#!/usr/bin/env python3
from pwn import xor
key = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(key)
flag = b'crypto{'
'''
b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'

'''
potentialKey = b'myXORkey'
print(xor(key, flag))
finalANswer = xor(key, potentialKey)

print(finalANswer)


# r = open("/usr/share/wordlists/rockyou.txt", "rb")

# print(r.readline())
# failSafe = 10
# i = 0
# for elem in r.readlines():
# 	print(elem)
# 	i += 1
# 	if i > failSafe:
# 		break 