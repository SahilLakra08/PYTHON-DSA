def funsum(n):
    if n == 0 :#BASE CONDITION
        return 0 #STOP
    else :#ACTUAL CODE
        return n+funsum(n-1)#CALL FUNCTION ITSELF
        
n=int(input('Enter the number: '))
a=funsum(n)
print('sum of N natural number through Recursion:' , a)