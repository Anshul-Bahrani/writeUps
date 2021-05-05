#!/usr/bin/env python3

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

e = 65537
x = 1
# ToFind:d
def modInverse(a, m):
	m0 = m
	y = 0
	x = 1
	print(f"m0={m0} y={y} x={x}")
	if (m == 1):
	    return 0
	print("Starting Iteration: ")
	while (a > 1):
		print("Iteration:")
		# q is quotient
		q = a // m

		t = m
		print(f"q={q} t={t}")
		# m is remainder now, process
		# same as Euclid's algo
		m = a % m
		a = t
		t = y
		print(f"m={m} a={a} t={t}")
		# Update x and y
		y = x - q * y
		x = t
		print(f"y={y} x={x}")
	print("Returning:x", x)
	# Make x positive
	if (x < 0):
		x = x + m0 
	return x

phiN = (p - 1)*(q - 1)
# print(modInverse(27, 392))
print(modInverse(e, phiN))

# 121832886702415731577073962957377780195510499965398469843281