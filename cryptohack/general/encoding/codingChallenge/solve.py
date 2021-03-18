#!/usr/bin/env python3


import telnetlib
import json
import base64
import codecs
from Crypto.Util import number

# while(True):
# 	print("[~] Sending", end="\r")

conn = telnetlib.Telnet("socket.cryptohack.org", 13377)

currentLevel = 0

def recvline():
    return conn.read_until(b"\n")

def readFromJson():
	encoding = recvline().decode()
	return json.loads(encoding)

def sendInJson(val):
    toSend = json.dumps(val).encode()
    # print("sending", toSend)
    conn.write(toSend)


def toSolve(type, encoded):
	toReturn = ""
	if type == "base64":
		toReturn = base64.b64decode(encoded.encode()).decode()
	elif type == "hex":
		toReturn = bytes.fromhex(encoded).decode()
	elif type == "rot13":
		toReturn = codecs.getencoder("rot-13")(encoded)[0]
	elif type == "bigint":
		# print(int(encoded, 16))
		toReturn = number.long_to_bytes(int(encoded, 16)).decode()
	elif type == "utf-8":
		toReturn = "".join([chr(x) for x in encoded])
	return toReturn
	# print(type, toReturn)

# toSolve("base64", "SGk=")
# toSolve("hex", "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
# toSolve("rot13", "uryyb")
# toSolve("bigint", "0x6a655f64697374616e745f72656e6577")
# toSolve("utf-8", [116, 97, 108, 101, 110, 116, 95, 109, 97, 112, 108, 101, 95, 105, 110, 100, 101, 120, 101, 100])
'''
base64
hex
rot13
bigint
utf-8


'''
# while(True):
# 	print("[~] Sending", end="\r")


while(currentLevel < 100):
	ip = readFromJson()
	# print(ip)
	# print(ip['type'])
	typeOfEncoding = ip['type']
	toSend = dict()
	toSend["decoded"] = toSolve(ip["type"], ip["encoded"])
	print(f"[~] Sending {currentLevel}/100", end="\r")
	sendInJson(toSend)
	currentLevel += 1


print("\nPerhaps the flag-", recvline().decode())


'''

Perhaps the flag- {"flag": "crypto{3nc0d3_d3c0d3_3nc0d3}"}


pwntools modifying the print function is a suspension which is dued for a later date

'''