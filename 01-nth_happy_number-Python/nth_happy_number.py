# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

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

def nth_happy_number(n):
	c=0
	f=0
	while(f<n):
		c+=1
		if(ishappynumber(c)):
			f=f+1
		
	return c

