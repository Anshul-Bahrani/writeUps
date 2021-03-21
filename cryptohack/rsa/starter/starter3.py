#!/usr/bin/env python3

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
# totient is the euler's phi function:

# phi(n) = phi(p*q) = phi(p)*phi(q)
# and since p and q are prime numbers, phi(prime) = prime - 1
print((p - 1)*(q - 1))