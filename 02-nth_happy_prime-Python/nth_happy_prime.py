# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

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
def ishappy(a):
	s=0
	while(a>0):
		r=a%10
		s+=r*r
		a//=10
	return s


def ishappynumber(n):
	# your code goes here
	a=b=n
	while(True):
		a=ishappy(a)
		b=ishappy(ishappy(b))
		if(a==b):
			break
	if(a==1):
		return True
	else:
		return False



def fun_nth_happy_prime(n):
	c=0
	f=0
	while(f<=n):
		c+=1
		if(ishappynumber(c) and isprime(c)):
			f=f+1
		
	return c