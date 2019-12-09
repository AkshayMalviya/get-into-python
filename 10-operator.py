#OPERATOR

#arithmetc operator
a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c = a - b
print ("Line 2 - Value of c is ", c)
c = a * b
print ("Line 3 - Value of c is ", c )
c = a / b
print ("Line 4 - Value of c is ", c)
c = a % b
print ("Line 5 - Value of c is ", c)
a = 2
b = 3
c = a**b 
print ("Line 6 - Value of c is ", c)
a = 10.0
b = 5
c = a//b 
print ("Line 7 - Value of c is ", c)

#comparision operator
a = 21
b = 10
c = 0
if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")
if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")
if ( a < b ):
   print ("Line 4 - a is less than b" )
else:
   print ("Line 4 - a is not less than b")
if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")
a = 5;
b = 20;
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to  b")
else:
   print ("Line 6 - a is neither less than nor equal to  b")
if ( b >= a ):
   print ("Line 7 - b is either greater than  or equal to b")
else:
   print ("Line 7 - b is neither greater than  nor equal to b")
print("-------------------------------------------------------")

#Assignment operator
a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c += a
print ("Line 2 - Value of c is ", c)
c *= a
print ("Line 3 - Value of c is ", c )
c /= a 
print ("Line 4 - Value of c is ", c)
c  = 2
c %= a
print ("Line 5 - Value of c is ", c)
c **= a
print ("Line 6 - Value of c is ", c)
c //= a
print ("Line 7 - Value of c is ", c)
print("-------------------------------------------------------")

#Bitwise operator
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)
c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)
c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)
c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)
c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)
c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
print("-------------------------------------------------------")


#membership operator
a=10
b=20
list=[1,2,3,4,5]
if(a in list):
	print("a is available in list")
else:
	print("a is not available in list")
if(b not in list):
	print("b is not available in the list")
else:
	print("b is available in the list")
a=2
if(a in list):
	print("a is available in the list")
else:
	print("a is not available in the list")
print("-------------------------------------------------------")

#identity membership
a=20
b=20
if(a is b):
	print("a and b same identity")
else:
	print("a and b not same identity")
if(id(a)==id(b)):
	print("a and b same identity")
else:
	print("a nd b not same identity")
b=30
if(a is b):
	print("a nd b same identity")
else:
	print("a nd b not same identity")
if(a is not b):
	print("a nd b not same identity")
else:
	print("a nd b same identity")
print("-------------------------------------------------------")

#operator precedence
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)
e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)
e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)
e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)