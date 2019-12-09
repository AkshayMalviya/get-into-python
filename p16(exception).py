#EXCEPTION



def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))



#Exception Handling
try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.



try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()



try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")



#The except Clause with Multiple Exceptions
try:
   You do your operations here
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.



#The try-finally Clause
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................



#Finally
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()




try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")



#Argument of an Exception
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")




#Raise an Exception
def functionName(level):
	if level<1:
		raise Exception(level)
	return level
try:
	l=functionName(-10)
	print("level =",l)
except Exception as e:
	print("Error in level argument",e.args[0])



#User Defined Exception
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e.args)
