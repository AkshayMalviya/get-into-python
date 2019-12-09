#DECISION MAKING


var1=100
if var1:
	print("True")
	print(var1)
else:
	print("False")

var2=0
if var2:
	print("True")
	print(var2)
else:
	print("Exit")



var = 100
if ( var  == 100 ) : print ("Value of expression is 100")
print ("Good bye!")



#While loop
count=0
while(count<9):
	print("The count is: ",count)
	count+=1
print("Hello")



var = 1
while var == 1 :  # This constructs an infinite loop
   num = input("Enter a number  :")
   print ("You entered: ", num)
print ("Hello")



count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")



flag = 1
while (flag): print ('Given flag is really true!')
print ("Good bye!")



#FOR Loop
for letter in 'Python':
	print("current letter: ",letter)
fruits=['banana','apple','mango']
for fruit in  fruits:
	print("current fruit: ",fruit)
print('Hello')



fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])
print('Hello')



#For with Else
for num in range(10,20):
	for i in range(2,num):
		if num%i==0:
			j=num/i
			print ('%d equals %d*%d '%(num,i,j))
			break
	else:
		print(num, 'is prime number')



#Nested Loop
#Prime Number
i=2
while (i<100):
	j=2
	while(j<=(i/j)):
		if not(i%j):break
		j=j+1
	if(j>i/j):print (i,' is prime')
	i=i+1
print('Hello')



#Break
for letter in 'python':
	if letter =='h':
		break
	print('Current Letter: ',letter)
var=10
while var>0:
	print('Current variable value: ',var)
	var=var-1
	if var==5:
		break
print("Hello")


