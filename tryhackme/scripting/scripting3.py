import socket
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
            Cipher, algorithms, modes
            )

ip = "10.10.15.204"

port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
def send(message):
	s.send(message.encode())
	return s.recv(4096)
# print(get_random_bytes(32))

# Generating random key of 256 bytes:(32*8)

key = get_random_bytes(32)
fileToStore = open("key.txt", "wb")
fileToStore.write(key)
fileToStore.close()

fileToStore = open("key.txt", "rb")

salt = fileToStore.read()
print(salt)

print(send("hello"))
print(send("ready"))
print(send("final"))

final = b"key:thisisaverysecretkeyl337 iv:secureivl337 to decrypt and find the flag that has a SHA256 checksum of ]w\xf0\x18\xd2\xbfwx`T\x86U\xd8Ms\x82\xdc'\xd6\xce\x81n\xdeh\xf6]rb\x14c\xd9\xda send final in the next payload to receive all the encrypted flags"

key = b"thisisaverysecretkeyl337"
iv = b"secureivl337"
tag = b"h\t:\xe9\xa3\x8d\xb8\xd3y.'\xc3\x1d"
checksum = b"]w\xf0\x18\xd2\xbfwx`T\x86U\xd8Ms\x82\xdc'\xd6\xce\x81n\xdeh\xf6]rb\x14c\xd9\xda"

checksum = base64.b16encode(checksum).lower()

print(checksum)
def decrypt(cipherText, tag):
	global key,iv
	decryptor = Cipher(algorithms.AES(key),modes.GCM(iv, tag),backend=default_backend()).decryptor()
	return decryptor.update(cipherText) + decryptor.finalize()

def getHash(text):
	hash_object = hashlib.sha256(text)
	hex_dig = hash_object.hexdigest()
	return hex_dig.encode()

while 1:
	cipherText = send("final")
	tag = send("final")
	print("Printing.....",cipherText, tag)
	try:
		flag = decrypt(cipherText, tag).decode()
	except:
		flag = "brbrb"
	decryptHash = getHash(flag.encode())

	if decryptHash == checksum:
		print("Flag : ", flag)
		break
