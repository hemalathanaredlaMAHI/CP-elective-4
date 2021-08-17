import math
def isprime(a):
	if(a<=1):
		return False
	elif(a==2):
		return True
	elif(a%2==0):
		return False
	else:
		for i in range(3,int(math.sqrt(a)),2):
			if(a%i==0):
				return False
		return True
def additive(n):
 
    s=0
    while(n>0):
        s=s+(n%10)
        n=n//10
    if(isprime(s)):
        return True
    return False
        
        
def isAdditivePrime(n):
    if(n<10 and isprime(n)):
        return True
    else:
        if(additive(n) and isprime(n)):
            return True
    return False











assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")