# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….
def revers(n):
	s=0
	while(n>0):
		r=n%10
		s=s*10+r
		n=n//10
	return s

def ispallindrom(n):
	if(revers(n)==n):
		return True
	return False


def islychrelnumber(n):
	for i in range(0,50):
		n+=revers(n)
		if ispallindrom(n):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	c=0
	i=1
	while(c!=n):
		if(islychrelnumber(i)):
			c+=1
		i+=1
	return i-1
