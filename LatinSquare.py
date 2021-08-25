# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    if(len(lst)==0):
        return False
    d=[i for i in range(1,len(lst)+1)]
    for i in lst:
        for j in d:
            if(j not in i):
                return False
    for i in range(0,len(lst)):
        t=[]
        for j in range(0,len(lst)):
            t.append(lst[j][i])
        for k in d:
            if k not in t:
                return False
    return True


assert(isLatinSquare([[1,2,3],[2,3,1],[3,1,2]])==True)
assert(isLatinSquare([[1,1,1],[1,1,1],[0,0,0]])==False)
assert(isLatinSquare([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])==True)
assert(isLatinSquare([])==False)
assert(isLatinSquare([[1,2,3],[4,5,6],[7,8,9]])==False)
assert(isLatinSquare([[1,2,3],[1,2,3],[1,2,3]])==False)
print("All Test cases passed..................")
