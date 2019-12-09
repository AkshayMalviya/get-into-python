#LIST

#FUNCTIONS

#CMP
x,y=[123,'xyz'],[456,'abc']
print(cmp(x,y))
print(cmp(y,x))
z=y+[789]
print(cmp(y,z))
print(z)



#LEN
x=list(range(5))
print(len(x))



#MAX, MIN
x,y=['a','b','d','c','aa'],[1,2,0.4,3]
print(max(x), max(y), min(x), min(y))



#LIST
atuple=(123,'abc',1.2)
alist=list(atuple)
print(alist)
str='Hello Python'
alist=list(str)
print(alist)



#METHODS


#APPEND
x=['C++','JAVA','PYTHON']
x.append('C#')
print(x)



#COUNT
x=['C++','JAVA','PYTHON',123,345,123,'C++']
print(x.count('C++'))
print(x.count(123))
print(x.count(345))



#EXTEND
x=['C++','JAVA','PYTHON',123,345,123,'C++']
y=list(range(5))
x.extend(y)
print(x)



#INDEX
x=['C++','JAVA','PYTHON',123,345,123,'C++']
print(x.index('C++'))
print(x.index(123))
print(x.index(346))



#INSERT
x=['C++','JAVA','PYTHON',123,345,123,'C++']
x.insert(2,'abc')
print(x)



#POP
x=['C++','JAVA','PYTHON',123,345,123,'C++']
x.pop(-2)
print(x)



#REMOVE
x=['C++','JAVA','PYTHON',123,345,123,'C++']
x.remove('JAVA')
print(x)



#REVERSE
x=['C++','JAVA','PYTHON',123,345,123,'C++']
x.reverse()
print(x)



#SORT
x=['C++','JAVA','PYTHON','C++']
x.sort()
print(x)
