# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

def largestperfectsquare(n):
	i=1
	p=0
	while(True):
		s=i*i
		if(n<s):
			return p
		elif(n==s):
			return s
		else:
			p=s
		i+=1
