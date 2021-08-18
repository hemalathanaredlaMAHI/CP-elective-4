# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	a=str1
	f=0
	while(True):
		if(a==str2):
			return True
		elif(a==str1 and f!=0):
			return False
		a=a[1:]+a[0:1]
		f=1
		