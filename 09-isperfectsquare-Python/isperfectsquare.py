# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	# your code goes here
	
		
	if(type(n)==type(1)):
		if(n<0):
			return False
		else:
			m=int(math.sqrt(n))
			if(m**2==n):
				return True
			return False
	elif(type(n)==type(1.2)):
		return False
	elif(n.isnumeric()==True):
		n=int(n)
		if(n<0):
			return False
		else:
			m=int(math.sqrt(n))
			if(m**2==n):
				return True
			return False
	else:
		return False


