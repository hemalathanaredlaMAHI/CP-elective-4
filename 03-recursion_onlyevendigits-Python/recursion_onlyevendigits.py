# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.


def onlyevendigits(l,v=0,i=0):
	if(l==0):
		return v
	if(l%2==0):
		v+=(10**i*(l%10))
		i+=1
	return onlyevendigits(l//10,v,i)


def fun_recursion_onlyevendigits(l): 
	new=[]
	if(len(l)==0):
		return []
	else:
		new.append(onlyevendigits(l[0]))
		return new+fun_recursion_onlyevendigits(l[1:])