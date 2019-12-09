#solution 1

import sys
#sys.setrecursionlimit(150000)
def fib(n):
	if n == 1 or n == 2:
		return n
	else:
		return fib(n-2) + fib(n-1)
print(fib(int(input("Enter the number: "))))


#---------------------------------------------------------
#solution 2

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
print(fib(int(input("Enter the number: "))))
