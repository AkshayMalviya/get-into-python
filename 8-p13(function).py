#FUNCTION


def printme(str):
	"This is print the passed string into this function"
	print (str)
	return
printme("Hello")



#Passed by Reference
def changeme(mylist):
	print("Value before change", mylist)
	mylist[2]=50
	print("Value after change", mylist)
mylist=[1,2,3,4,5]
changeme(mylist)
print("Value outside of function", mylist)



def changeme(mylist):
	print("Value before change", mylist)
	mylist=[4,5,6]
	print("Value after change", mylist)
mylist=[1,2,3]
changeme(mylist)
print("Value outside function", mylist)



#Function Argument


def printme(str):
	print(str)
	return
printme('Hello')



#Keyword Argument
def printme(str):
	print(str)
	return
printme(str="My string")



#Keyword Argument
def printme(name,age):
	print("Name:", name)
	print("age :", age)
printme(age=50,name='Aayush')



#Default Argument
def printinfo(name,age=35):
	print('Name:', name)
	print('Age :', age)
	return
printinfo(age=50,name='Aayush')
printinfo(name='Devesh')



#Variable Length Argument
def printinfo(arg,*vartuple):
	print("Output is: ")
	print(arg)
	for var in vartuple:
		print(var)
	return
printinfo(10)
printinfo(70,60,50)



#Lambda Function
#function definition
sum=lambda arg1,agr2:arg1+agr2
#call sum as a function
print(sum(10,20))
print(sum(20,30))
