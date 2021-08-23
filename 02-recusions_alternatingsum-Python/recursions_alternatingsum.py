# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def alternatingsum(s,sum,n):
	if(len(s)==0):
		return sum
	elif(n==1):
		sum+=s[0]
		return alternatingsum(s[1:],sum,-1)
	elif(n==-1):
		sum-=s[0]
		return alternatingsum(s[1:],sum,1)

def fun_recursions_alternatingsum(l): 
	sum=0
	return alternatingsum(l,sum,1)