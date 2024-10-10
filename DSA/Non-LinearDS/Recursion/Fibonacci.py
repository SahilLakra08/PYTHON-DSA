def fib(n):
    if (n == 0 or n ==1):  #OR   if(n == 1 or n == 2):
        return n
    else:
        return fib(n-1)+fib(n-2)

n = int(input('Enter the Nth number for fibonacci : '))
a=fib(n)
print('Fibonacci Number: ',a)