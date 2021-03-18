#!/usr/bin/env python3

from Crypto.Util import number

'''

Python's PyCryptodome library implements this with the methods Crypto.Util.number.bytes_to_long and Crypto.Util.number.long_to_bytes.

Crypto is the name of the packageeee

'''

inputString = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"


print(number.long_to_bytes(inputString))

'''
b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
'''