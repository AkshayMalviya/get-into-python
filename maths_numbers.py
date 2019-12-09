#NUMBERS



#ABSOLUTE VALUE
print(abs(-45))
print(abs(100.12))
#print(abs(9L))



#CEIL
import math
print(math.ceil(12.45))
print(math.ceil(-45.17))
print(math.ceil(math.pi))


#EXPONENTIAL
import math
print(math.exp(-2))
print(math.exp(100.12))
print(math.exp(math.pi))



#FABS
import math
print(math.fabs(-45.17))
print(math.fabs(100.12))
print(math.fabs(math.pi))



#FLOOR
import math
print(math.floor(-2.1))
print(math.floor(10.25))
print(math.floor(math.pi))



#Natural LOG
import math
print(math.log(100.12))
print(math.log(12))
print(math.log(math.pi))



#MAX & MIN
print(max(1,2,4,3))
print(max(-1,-3,-2))
print(max(0,1,-1,5))
print(min(1,2,4,3))
print(min(-1,-3,-2))
print(min(0,1,-1,5))



#MODF
import math
print(math.modf(1.29))
print(math.modf(1.72))
print(math.modf(math.pi))



#POW
import math
print(math.pow(100,2))
print(math.pow(100,-2))
print(math.pow(2.1,2))
print(math.pow(3,0))



#ROUND
import math
print(round(80.23656789,2))
print(round(1212.2123233213123,3))
print(round(math.pi,3))



#SQRT
import math
print(math.sqrt(100))
print(math.sqrt(7))
print(math.sqrt(math.pi))


#RANDOM FUNCTION
#---------------


#CHOICE
import random
print(random.choice([1,2,3,4,5,6,7,8,9,0]))



#RANDRANGE
import random
print(random.randrange(100,1000,2))
print(random.randrange(100,1000,3))



#RANDOM
import random
print(random.random())



#SHUFFLE
import random
list=[20,12,16,52]
random.shuffle(list)
print(list)



#UNIFORM
import random
print(random.uniform(2,20))




#Trignometry Function
#
import math
print(math.acos(.2))
print(math.asin(.6))
print(math.atan(10))
print(math.atan2(10,20))
print(math.cos(0))
print(math.cos(2*math.pi))
print(math.hypot(3,4))
print(math.tan(math.pi/4))
print(math.degrees(3))
print(math.radians(3))
