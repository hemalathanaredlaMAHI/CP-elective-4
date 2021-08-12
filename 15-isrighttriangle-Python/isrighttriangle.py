# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def distance(x1,y1,x2,y2):
	r= math.sqrt((x2-x1)**2+(y2-y1)**2)
	return r
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a=distance(x1,y1,x2,y2)
	b=distance(x2,y2,x3,y3)
	c=distance(x3,y3,x1,y1)
	m=max(a,b,c)
	if(math.isclose(a**2+b**2+c**2-m**2,m**2)):
		return True
	return False
