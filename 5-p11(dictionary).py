#DICTIONARY


#Empty Dictionary
dict={}
print(dict)



#Example
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict['Name'],dict['Age'],dict['Place'])
for i in dict:
	print(dict[i])



#Updating Dictionary
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
dict['Age']=22
dict['School']='Excellence'
for i in dict:
	print(dict[i])
del dict['Name']#remove particulare entry
print(dict)
dict.clear()		#remove all entry
print(dict) 		


#Duplicate Value
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
print(dict['Name'])



#IN
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print('Name' in dict)



#NESTED DICTIONARY
dict={'Name':{1:'Akshay',2:'Aayush'},'Age':{1:23,2:24},'Place':{1:'Indore',2:'Ujjain'}}
print(dict['Name'][1])


#Built-in Dictionary Function


#LEN
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
print(len(dict))



#STR
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
print(str(dict))



#TYPE
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
print(type(dict))
x=1
print(type(x))



#DICTIONARY METHODS



#CLEAR
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
dict.clear()
print(dict)



#COPY
dict={'Name':'Akshay','Age':23,'Place':'Indore','Name':'Aayush'}
dict2=dict.copy()
print(dict2)



#FROMKEYS
seq=('Name','Age','Sex')
dict=dict.fromkeys(seq)
print(str(dict))
dict=dict.fromkeys(seq,'Akshay')
print(str(dict))



#GET
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.get('Age'))
print(dict.get('Sex'))



#ITEMS
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.items())



#KEY
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.keys())



#SETDEFAULTS
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.setdefault('Age',None))
print(dict.setdefault('Sex',None))
print(dict)



#UPDATE
dict1={'Name':'Akshay','Age':23,'Place':'Indore'}
dict2={'Sex':'Male'}
dict1.update(dict2)
print(dict1)



#VALUES
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.values())



#POP, POPITEM
dict={'Name':'Akshay','Age':23,'Place':'Indore'}
print(dict.pop('Place'))
print(dict)
print(dict.popitem())
print(dict)

