# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def ispronic(x):
	for i in range(1,x//2+1):
		if((i*(i+1))==x):
			return True
	return False


def nthpronicnumber(n):
	x=0
	f=0
	while(f<n):
		x+=1
		if(ispronic(x)):
			f+=1
	return x

print(nthpronicnumber(1))