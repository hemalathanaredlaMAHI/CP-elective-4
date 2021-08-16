# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	n=abs(n)
	if(n<=10):
		return False
	else:
		n=str(n)
		for i in range(0,len(n)-1):
			if(n[i] in n[i+1:]):
				return True
		return False
