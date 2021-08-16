# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	if(len(a)==0):
		return -1
	a.sort()
	
	l=[]
	for i in range(0,len(a)-1):
		d=a[i]-a[i+1]
		l.append(d)
	l.sort(reverse=True)
	return abs(l[0])
	