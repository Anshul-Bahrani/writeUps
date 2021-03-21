#!/usr/bin/env python3

def gcdExtended(a, b): 
 
    # Base Case 
    if a == 0 :  
        return b, 0, 1
            
    gcd, x1, y1 = gcdExtended(b%a, a) 
    
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
    
    return gcd, x, y


p = 26513
q = 32321

g, u, v = gcdExtended(p, q)
print(u, v)