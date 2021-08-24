# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
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

def sumOfSquaresOfDigits(n):
    if(n<10):
        return n
    else:
        re=0
        while(n>0):
            r=n%10
            re+=(r*r)
            n=n//10
        return sumOfSquaresOfDigits(re)


def ishappy(n):
    if(sumOfSquaresOfDigits(n)==1):
        return True
    return False



def ishappyprimenumber(n):
    if(ishappy(n) and isprime(n)):
        return True
    return False