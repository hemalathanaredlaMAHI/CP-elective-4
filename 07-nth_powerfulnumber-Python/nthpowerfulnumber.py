# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def prime(n):
  if(n==2):
    return True
  elif(n<2 or n%2==0):
    return False
  fac=round(math.sqrt(n))
  for i in range(3,fac+1,2):
    if(n%i==0):
      return False
  return True

def ispowerful(n):
  if(n==1):
    return True
  count=0
  count1=0
  for i in range(2,int(n//2)+1):
    if(n%i==0 and prime(i)):
      count+=1
      if n%(i*i)==0:
        count1+=1
  if(count==count1 and count!=0):
      return True
  return False

def nthpowerfulnumber(n):
	c=0
	found=0
	while(n>=found):
		c=c+1
		if(ispowerful(c)):
			found+=1
	return c

