#TUPLE


#Single Value
tup=(16,)
print(tup)



#ACCESING
tup1=('physics','chemistry' ,1997,2000)
tup2=(1,2,3,4,5,6,7)
print(tup1[0])
print(tup2[1:5])



#ADDITION OF TUPLE
tup1=(12,34,56)
tup2=('abc','xyz')
tup3=tup1+tup2
print(tup3)



#DELETION OF ELEMENT
tup1=('physics','chemistry' ,1997,2000)
print(tup1)
del tup1
print('After Deletion: ')
print(tup1)



#GENERAL OPERATION
x=(1,2,3)+(4,5,6)
print(x)
print(x*2)
print(len(x))
print( 3 in x )
for i in x:
	print(i,end='')



#FUNCTIONS IN TUPLE

#LEN
x,y=(123,'abc',0.45),(456,'xyz')
print(len(x),len(y))



#MAX, #MIN
x,y=('abc','def','e'),(123,345,8)
print(max(x),max(y))
print(min(x),min(y))



#TUPLE
x=['xyz',123,0.98,'%']
print(tuple(x))
