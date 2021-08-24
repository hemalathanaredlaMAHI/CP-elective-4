# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
import math

def isprime(n):
    if(n==2):
        return True
    elif(n%2==0 or n<2):
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True
    
def SumOfDigits(n):
    if(n<10):
        return n
    else:
        s=0
        while(n>0):
            r=n%10
            s+=r
            n=n//10
        return s

def issmith(n):
    d=SumOfDigits(n)
    r=0
    i=2
    while(i*i<=n):
        if(n%i==0):
            n//=i
            r=r+SumOfDigits(i)
        else:
            i+=1
    r+=SumOfDigits(n)
    if(d==r):
        return True
    return False


def fun_nth_smithnumber(n):
    found=-1
    got=0
    while(found<=n):
        got+=1
        if(issmith(got) and isprime(got)==False):
            found+=1
    return got

    