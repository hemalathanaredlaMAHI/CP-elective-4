# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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

def fun_nearestkaprekarnumber(n):
    a=n
    b=n
    if(iskaprekarnumber(n)):
        return n
    while(True):
        a=a-1
        b=b+1
        if(iskaprekarnumber(a)):
            return a
        if(iskaprekarnumber(b)):
            return b

    return 1
