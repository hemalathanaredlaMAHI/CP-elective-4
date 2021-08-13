# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit=abs(digit)
	if(len(str(digit))<=k):
		return 0
	c=0
	while(digit>0):
		r=digit%10
		if(c==k):
			return r
		c+=1
		digit//=10


