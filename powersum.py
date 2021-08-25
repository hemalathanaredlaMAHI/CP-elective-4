# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k) or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def power(a, b):
    result=1
    while(b>0):
        if((b & 1) == 1) :
            result=result*a
        b=b>>1
        a=a*a
    return result
    # if b == 0:
    #     return 1
    # else:
    #     return a * power(a, b-1)



def powerSum(n, k):
    # Your code goes here...
    if(n<0 or k<0):
        return 0
    else:
        s=0
        for i in range(1,n+1):
            s+=power(i,k)

    return s

# Write your own test cases here...
assert(powerSum(2,10) == 1025)
assert(powerSum(3,10) == 60074)
print ("All test cases passed...")
