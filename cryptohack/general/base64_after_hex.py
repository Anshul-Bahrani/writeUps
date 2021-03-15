#! /bin/python3

import base64
# this is a hex string
inputString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

inputString = bytes.fromhex(inputString)

print(inputString)


print(base64.b64encode(inputString))

print(base64.b64encode(b"hello"))

'''
b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'
b'crypto/Base+64+Encoding+is+Web+Safe/'
b'aGVsbG8='


'''