#!/usr/bin/env python3

from math import pow

privateKey = 121832886702415731577073962957377780195510499965398469843281
#Found from previous challenge

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
# To Decrypt:
c = 77578995801157823671636298847186723593814843845525223303932

print((pow(c,privateKey)))