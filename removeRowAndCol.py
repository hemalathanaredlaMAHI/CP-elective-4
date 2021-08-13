# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

# list
# [ [ 2, 3, 4, 5],
#   [ 8, 7, 6, 5],
#   [ 0, 1, 2, 3] ]

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]

def removeRowAndCol(L, row, col):
    # Your code goes here...
    if(row<0 or col<0 or len(L)==0 or len(L)<row or len(L)<col):
        return None
    else:
        del L[row]
        for i in range(0,len(L)):
            del L[i][col]
        return L

   

# Write your own test cases.

assert(removeRowAndCol([[2,3,4,5],[8,7,6,5],[0,1,2,3]],1,0)==[[3,4,5],[1,2,3]])
assert(removeRowAndCol([[2,3,4,5],[8,7,6,5],[0,1,2,3]],1,2)==[[2,3,5],[0,1,3]])
assert(removeRowAndCol([[2,3,4,5],[8,7,6,5],[0,1,2,3]],-1,-2)==None)
assert(removeRowAndCol([[2,3,4,5],[8,7,6,5],[0,1,2,3]],6,7)==None)
assert(removeRowAndCol([],1,2)==None)
print("All test cases passed ..........")