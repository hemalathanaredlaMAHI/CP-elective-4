# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 
def powerof3ton(n,i,l):
	if(3**i>n):
		return l
	else:
		r=3**i
		i+=1
		l.append(r)
		return powerof3ton(n,i,l)


def recursion_powersof3ton(n):
	if(n<1):
		return None
	else:
		return powerof3ton(n,0,[])

