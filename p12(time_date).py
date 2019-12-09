#TIME AND DATE



#TIME
import time
ticks=time.time()
print(ticks)
print('---------------------------------------')
print(time.localtime())
print('---------------------------------------')
print(time.localtime(time.time()))
print('---------------------------------------')
print(time.asctime(time.localtime(time.time())))
print('---------------------------------------')



#CALENDAR
import calendar
cal=calendar.month(2017,7)
print(cal)


###########################

#Time Methods


#altzone
import time
print(time.altzone)



#asctime
import time
t=time.localtime()
print(time.asctime(t))



#clock
import time
def procedure():
	time.sleep(2.5)
t1=time.clock()
procedure()
print(time.clock()-t1, 'Seconds Process Time')
t2=time.time()
procedure()
print(time.time()-t2, 'Seconds Wall Time')



#ctime
import time
print(time.ctime())



#gmtime
import time
print(time.gmtime(1455508609.34375))
print(time.gmtime())



#localtime
import time
print(time.localtime())



#mktime
import time
t=(2017,8,1,10,13,38,1,48,0)
d=time.mktime(t)
print(d)
print(time.asctime(time.localtime(d)))



#sleep
import time
print(time.ctime())
time.sleep(5)
print(time.ctime())



#strfftime
import time
t=(2015,12,31,10,39,45,1,48,0)
t=time.mktime(t)
print(time.strftime('%b %d %Y %H %M %S',time.localtime(t)))



