#STRING


var1='Hello World'
var2='Python Programming'
print(var1)			#Whole String
print(var2[1:5])	#from character 2 to next 5
print(var1[:5]+' '+var2[:6])
print('My Name is %s'%('khan'))



para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)



#print('C:\\python')
#print(r'C:\\python')



#UNICODE STRING(16-BIT)
print(u'Hello World')



#CAPITALIZE
str='this is simple string'
print(str.capitalize())



str='This string is centered now......WOW!!'
print(str.center(50,'a'))



#SUBSTRING FINDING
str='this is string example...WOW!!!'
substr='i'
print(str.count(substr,0,len(str)))
substr1='is'
print(str.count(substr1))



#ENCODE, DECODE
str='This is encoded string example'
str1=str.encode('base64','strict')
print('Encoded String: '+str1)



#INDEX
str1='This is string Example'
str2='Exam'
print(str1.index(str2))
print(str1.index(str2,10))
print(str1.index(str2,16))



#ENDSWITH
str='This is String Example......WOW!!'
suffix='WOW!!'
print(str.endswith(suffix))
print(str.endswith(suffix,20))
suffix='is'
print(str.endswith(suffix,2,4))
print(str.endswith(suffix,2,5))



#FIND
str1='This is string Example....WOW!!!'
str2='Exam'
print(str1.find(str2))
print(str1.find(str2,10))
print(str1.find(str2,40))



#ISALNUM, ISALPHA, ISDIGIT, ISLOWER, ISNUMERIC, ISSPACE, ISTITLE
str='this2017'
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isnumeric())
print(str.isspace())
str='this is simple string'
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isnumeric())
print(str.isspace())
str='1234567890'
print(str.isdigit())
print(str.isnumeric())
print(str.isspace())
str=' '
print(str.isspace())
str='This Is String'
print(str.istitle())



#ISUPPER
str='THIS IS UPPER CASE STRING'
print(str.isupper())
str='THIS IS DEFECTED STring'
print(str.isupper())
str='THIS IS ANOTHER STRING1'
print(str.isupper())



#JOIN
s='-'
seq=('a','b','c')
print(s.join(seq))
 


#LENGTH
str='This method return length of string'
print(len(str))



#LJUST(left justified), RJUST,LOWER
str='This is Left justified string'
print(str.ljust(50,'*'))
print(str.rjust(50,'*'))
print(str.lower())



#LSTRIP, RSTRIP
string='*****This is stripped string***********'
print(string.lstrip('*'))
print(string.rstrip('*'))



#MAKETRANS
intab='aeiou'
outtab='12345'
transtab=str.maketrans(intab,outtab)
str='This is string example.....WOW!!!'
print(str.translate(transtab))



#MAX, MIN, replace
string='This is a string example....is really!!!'
print("Max character: "+max(string))
print("Min character: "+min(string))
print(string.replace('is','was',2))
string='Thisisastringexample....WOW!!!'
print("Max character: "+max(string))
print("Min character: "+min(string))



#RFIND, RINDEX
str1='This is really a string Example....WOW!!!'
str2='is'
print(str1.rfind(str2))
print(str1.rfind(str2,0,10))
print(str1.rfind(str2,10,0))
print(str1.find(str2))
print(str1.find(str2,0,10))
print(str1.find(str2,10,0))

print(str1.rindex(str2))
print(str1.rindex(str2,5,20))



#SPLIT, SPLITLINES
string='This is String Example...wow!!!'
print(string.split())
print(string.split('i',1))

string='This is \nString example.....\nWOW!!!'
print(string.splitlines())
num=string.count('\n')
print(string.splitlines(num))



#STARTWITH
string='This is string example....WOW!!!'
print(string.startswith('This'))
print(string.startswith('string',8))
print(string.startswith('This',2,4))



#STRIP
str='**********this * is string example************'
print(str.strip('*'))



#SWAPCASE, TITLE
str='ThiS iS ThE StrInG'
print(str.swapcase())
str='this is the string example'
print(str.title())



#TRANSLATE
from string import maketrans
intab='aeiou'
outtab='12345'
transtab=maketrans(intab,outtab)
str='This is string example....wow!!!'
print(str.translate(transtab))


#UPPER, ZFILL, ISDECIMAL
str1='This is string example111'
str2='12435647556'
print(str1.upper())
print(str1.zfill(50))
print(str1.isdecimal())
print(str2.isdecimal())