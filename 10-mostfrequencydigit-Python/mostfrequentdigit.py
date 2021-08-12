# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	d=dict()
	while(n>0):
		r=n%10
		if r in d:
			d[r]+=1
		else:
			d[r]=1
		n//=10
	m=0
	r=0
	d=dict(sorted(d.items()))
	for i in d:
		if(d[i]>m):
			m=d[i]
			r=i
	return r

