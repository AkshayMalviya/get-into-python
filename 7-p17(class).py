#CLASSES AND OBJECTS


#General Example

class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print ('Hello, my name is', self.name)

P=Person('Akshay')
P.sayHi()



class Employee:
	empCount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1
	def displayCount(self):
		print("Total Employee: ",Employee.empCount)
	def displayEmployee(self):
		print("Name: ",self.name," Salary: ",self.salary)
emp1=Employee("Zara",2000)
emp2=Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: ",Employee.empCount)



#Another Version
class Employee:
	empCount=0
	def displayCount(self):
		print("Total Employee: ",Employee.empCount)
	def displayEmployee(self,name,salary):
		print("Name: ",name," Salary: ",salary)
emp1=Employee()
emp2=Employee()
emp1.displayEmployee("Zara",2000)
emp2.displayEmployee("Manni",5000)
print("Total Employee: ",Employee.empCount)




class Employee:
	'Common base class for all Employee'
	empCount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1
	def displayCount(self):
		print("Total Employee: ",Employee.empCount)
	def displayEmployee(self):
		print("Name: ",self.name,"Salary: ",self.salary)
emp1=Employee("Zara",2000)
emp2=Employee("Manni",5000)
print("Doc: ",Employee.__doc__)
print("Name: ",Employee.__name__)
print("MOdule: ",Employee.__module__)
print("Bases: ",Employee.__bases__)
print("Dict: ",Employee.__dict__)



#Object Destroyed
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name," Destroyed")
pt1=Point()
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3))
del pt1
del pt2
del pt3



#CLASS INHERITANCE
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



#Check SubClass SuperClass
class A:
	print("A")
objA=A()
class B:
	print("B")
class C(A):
	def __init__(self):
		x=issubclass(C,A)
		print(x)
		x=issubclass(C,B)
		print(x)
		y=isinstance(objA,A)
		print(y)
		y=isinstance(objA,B)
		print(y)
obj=C()



#Overriding Method
class Parent:
	def myMethod(self):
		print("Hello Parent")
class Child(Parent):
	def myMethod(self):
		print("Hello Child")
c=Child()
c.myMethod()



#Operator Overloading
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)



#Data Hiding
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount)
print (counter.__secretCount)
