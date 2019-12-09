#FILE IO


fo=open("test3.txt","r+")
print("Name of the file: ",fo.name)
print("Closed or Not: ",fo.closed)
print("Opening mode: ",fo.mode)

#to write file
#fo.write("Python is great Language")

#to read file
str=fo.read()
print("Read String: ",str)
str1=fo.read()
print(str1)

#to check current position
position=fo.tell()
print("Current file position: ",position)

#repoisiotn pointer at begining once again
position=fo.seek(0,0)
str=fo.read(10)
print("Again read String: ",str)

fo.close()
print("Closed or Not: ",fo.closed)



#Renaming file
import os
os.rename("test3.txt","test.txt")
print("New File name: ",os.name)



#Remove
import os
os.remove("test2.txt")



#Directory
import os
#os.mkdir("Auto Create Dir")	#Make Dir
#os.chdir("/Phone")				#Chnage Dir
#os.getcwd()					#Get Current Dir
#os.rmdir("Auto Create Dir")
