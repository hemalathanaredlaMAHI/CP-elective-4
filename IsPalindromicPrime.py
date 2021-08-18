import math

def isprime(a):
	if(a<=1):
		return False
	elif(a==2):
		return True
	elif(a%2==0):
		return False
	else:
		for i in range(3,int(math.sqrt(a))+1,2):
			if(a%i==0):
				return False
		return True

def isrevers(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n//=10
    return s



def isPalindromicPrime(n):
    if(isprime(n) and isrevers(n)==n):
        return True
    return False








assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-")