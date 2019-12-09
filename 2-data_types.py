
str = 'Hello World!'	
print (str)				#complete string
print (str[0])			#first character
print (str [2:5])		#from 3 to 5
print (str[2:])			#from 3 to end
print (str*2)			#two times
print (str+"Test")		#concatenate Test



#LIST
list =['abcd', 786, 2.33, 'john', 70.2]
tinylist=[123,'aayush']
print (list)			#complete list
print (list[0])			#first element of list
print (list[1:3])		#from element 2 to element 3
print (list[2:])		#from element 3 to end
print (tinylist*2)		#print list 2 times
print (list+tinylist)	#concatenate

list[1]=123
print (list)			#updated list



#TUPLE
tuple=('abcd', 786, 2.33, 'john', 70.2)
tinytouple=(123,'aayush')
print (tuple)			#complete tuple
print (tuple[0])		#first element only
print (tuple[1:3])		#from element 2 to 3
print (tuple[2:])		#from element 3 to end
print (tinytouple*2)	#2 times
print (tuple+tinytouple)#concatenate
#tuple[1]=123			#invalid statement
#print (tuple)



#DICTIONARY
dict={}
dict['one']="This is one"
dict[2]="This is two"
tinydict={'name':'aayush','code':'AK47','dept':'jewel'}
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())
