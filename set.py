# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    ls=[]
    ls.append({})
    for i in range(1,n+1):
        for j in range(1,(n+1)-(i-1)):
            temp=[]
            for x in range(j,j+i):
                temp.append(x)
                
            if(len(ls)<k):
                ls.append(set(temp))
            else:
                return ls
    if(len(ls)==k):
        return ls
    else:
        return None
    



assert(limitedPowerSet(5,16)==[{}, {1}, {2}, {3}, {4}, {5}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {1, 2, 3, 4}, {2, 3, 4, 5}, {1, 2, 3, 4, 5}])
assert(limitedPowerSet(0,3)==None)
assert(limitedPowerSet(0,1)==[{}])
assert(limitedPowerSet(5,3)==[{}, {1}, {2}])
assert(limitedPowerSet(3,3)==[{}, {1}, {2}])
assert(limitedPowerSet(7,17)==[{}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {1, 2, 3}, {2, 3, 4}, {3, 4, 5}])
print("All Test cases passed................")
