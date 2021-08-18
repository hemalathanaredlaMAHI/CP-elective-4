"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    l=0
    h=len(input_array)
    m=(l+h)//2
    while(l<=h):
        if(value==input_array[m]):
            return m
        elif(value<input_array[m]):
            h=m-1
        else:
            l=m+1
        m=(l+h)//2

    return -1
