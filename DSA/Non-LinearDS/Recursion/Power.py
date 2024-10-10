def power(a,b):
    if(b == 0):
        return 1
    else:
        return a*power(a,b-1)
        
a=int(input('Enter the number A, where A^b: '))
b=int(input('Enter the number B, where A^b: '))
c=power(a,b)
print('Power A^b: ', c)