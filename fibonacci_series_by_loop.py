from datetime import datetime

def fib(n):
    a, b = 0, 1
    for i in range(1, n+1):
    	a, b = b, a + b
    	print(i,a,'\n')
    return a

input_value = int(input("Enter the number: "))
start_time = datetime.now()
x = fib(input_value)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
file_append = open('D:/fib.txt','w')
file_append.write(str(x))
file_append.write('\nTime to compute: '+str(end_time - start_time))
file_append.close()