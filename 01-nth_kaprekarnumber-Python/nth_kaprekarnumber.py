# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def iskaprekarnumber(n):
    s=n**2
    i=0
    s1=0
    while(s>0):
        r=s%10
        s1=s1+(r*(10**i))
        i+=1
        s=s//10
        if(s+s1==n and s1!=0):
            return True
    return False
def fun_nth_kaprekarnumber(n):
    c=0
    f=0
    while(f<=n):
        c+=1
        if(iskaprekarnumber(c)):
            f+=1
    return c
