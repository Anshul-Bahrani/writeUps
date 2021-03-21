#!/usr/bin/env python3

from PIL import Image

flag = Image.open("flag.png", "r")

flagHeight, flagWidth = flag.size

# print(flagHeight, flagWidth)

lemur = Image.open("lemur.png", "r")

lemurHeight, lemurWidth = lemur.size

# print(lemurHeight, lemurWidth)

flagPixels = list(flag.getdata())
lemurPixels = list(lemur.getdata())
# print(flagPixels)

answer = Image.open("answer.png")

answerPixels = list(answer.getdata())

# print(len(answerPixels), flagPixels[0])

for ind in range(len(flagPixels)):
	rgb = list()
	#R
	rgb.append(flagPixels[ind][0] ^ lemurPixels[ind][0])
	#G
	rgb.append(flagPixels[ind][1] ^ lemurPixels[ind][1])
	#B
	rgb.append(flagPixels[ind][2] ^ lemurPixels[ind][2])
	# print(tuple(rgb))
	answerPixels[ind] = tuple(rgb)

im2 = Image.new(answer.mode, answer.size)
im2.putdata(answerPixels)

im2.save("answer.png")