def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


n=int(input('Enter the Number for factorial :'))
a=fac(n)
print('Factorial :',a)
#find  nCr
r=int(input('n>r and r='))
result = fac(n)/fac(r)*fac(n-r)
print('nCr : ',result)