# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	def isproperty309(n):
	l="0123456789"
	p=n**5
	for i in l:
		if(i not in str(p)):
			return False
	return True
def nthwithproperty309(n):
	f=0
	x=308
	while(f<=n):
		x+=1
		if(isproperty309(x)):
			f+=1

	return x
