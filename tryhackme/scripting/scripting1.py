import base64
message = open("b64.txt", "r")
for line in message:
    decoded = line
for i in range(50):
    decoded = base64.b64decode(decoded)
print(decoded)