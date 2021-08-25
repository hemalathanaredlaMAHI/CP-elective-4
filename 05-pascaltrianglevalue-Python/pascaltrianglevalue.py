# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if(row<col or row<0 or col<0):
		return 0
	for line in range(1, row + 2):
		c=1 
		for i in range(1, line + 1):
			if(i==col+1 and line==row+1):
				return c
			c=int(c*(line-i)/i)
	
