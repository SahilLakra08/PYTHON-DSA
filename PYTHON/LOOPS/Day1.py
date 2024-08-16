num=int(input('Enter a number'))
r1=num*1
r2=num*2
r3=num*3
r4=num*4
r5=num*5
r6=num*6
r7=num*7
r8=num*8
r9=num*9
r10=num*10
print(num'*1',r1)


'''
'''
num=int(input('Enter Number='))
acount=5
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1
print(num,'*',acount,'=',num*acount)
acount=acount+1


'''
'''
n=int(input('Enter the number'))

for i in range(1,n+1):
    print(i,end="  ")
'''

'''
n=int(input("Enter the number"))

for i in range(1,n+1):
    if(n%i==0):
        print(i,end="  ")
'''
'''
n=int(input("Enter the number"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+10
if(count==2):
    print("THE NUMBER IS PRIME")
else
    print("THE NUMBER IS NOT PRIME")
    
''' 
'''
n=int(input("ENTER A NUMBER"))
for i in range(2,n):
    if (n%i==0):
        print("not prime")
        exit(0)
        
print("its prime")        
        
  '''
'''
num=int(input('ENTER THE NUMBER'))
num1=num
l=num%10
num=num//10
s=num%10
num=num//10
f=num%10
num=num//10

sum=l*3+s3+f*3 

if (sum==num1):
  print('THE number is armstrong')
else:
  print('the number is not armstrong')
'''


'''
series sum
'''
'''
x=int(input('Enter a number:'))
n=int(input('Enter a number:'))  
sum1=1
for i in range (1,n+1,2):
    sum1=sum1+(x**i)/i
    sum1+=(x**i)/i
    
print("sum:",sum1)
'''
'''
x=int(input('Enter a number:'))
n=int(input('Enter a number:')) 
sum1=0
for i in range (1,n+1,4):
    sum1=sum1+(x**i)/i



sum2=0
for i in range (3,n+1,4):
    sum2=sum2-(x**i)/i
    

sum3=sum1+sum2

print("sum:",sum3)
'''
'''

x=int(input('Enter a number:'))
n=int(input('Enter a number:')) 
sum1=0
sign=1
for i in range (1,n+1,2):
    sum1=sum1+(x**i)/i*sign
    sign=-sign
print("sum",sum1)    
    
'''
#sum series

n=int(input("ENTER THE NUMBER:"))
gsum=0 
for i in range(1,n+1):
    sum1=0 
    for j in range(1,i+1):
        sum1=sum1+j 
    gsum=gsum+sum1
    
print(gsum)





gsum=0