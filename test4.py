value = 'abc ijk'
intab='!'
outtab=' '
str =''.join(chr(ord(letter)+1) for letter in value)
print(str)
transtab=str.maketrans(intab,outtab)
print(str.translate(transtab))