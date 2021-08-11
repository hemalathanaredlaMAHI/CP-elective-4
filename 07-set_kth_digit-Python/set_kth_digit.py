# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	c=0
	s=0
	n1=abs(n)
	while(n1>0):
		r=n1%10
		if(c==k):
			s=d*10**c + s
		else:
			s=r*10**c + s
		c=c+1
		n1//=10
	if(k>=len(str(abs(n)))):
		s=d*10**k + s
	if(n<0):
		return -s
	return s

