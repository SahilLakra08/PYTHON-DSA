'''
#   WHILE LOOP
x=2
while(x<=100):
    print(x)
    x=x+2
'''
'''
#AND OR OPERATOR
qualification=input("ENTER YOUR QUALIFICATION: ")
experience=int(input("ENTER YOUR EXPERIENCE: "))
if(qualification=="PG"and experience>=3)or(qualification=="G"and experience>=5):
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
'''
'''
#PRIME NUMBERS WITH THE HELP OF WHILE LOOP:
x=int(input('ENTER YOUR NUMBER: '))
count=0
i=1
while(i<=x):
    if(x%i==0):
        print(i)
        count=count+1
    i=i+1
if(count==2):
    print("IT IS A PRIME NUMBER ")
else:
    print("IT IS A COMPOSITE NUMBER ")
'''
#REVERSE LOOPING note: ONE FOR LOOP ==3WHILE
'''
for i in range(10,0,-1):
    print(i)
    print(i,end='')
    print('_'*80)
'''
'''
i=10
while(i>0):
    print(i)
    i-=1
'''
'''
#EVERY FOR LOOP CAN BE WHILE LOOP BUT NOT VICE VERSA EXCEPT FIBBONACI SERIES
a=0
b=1
c=a+b
print(a)
print(b)
while(c<=500):
    print(c)
    a=b
    b=c
    c=a+b
''' 
#BY FOR LOOP
'''
a=0
b=1
print(a)
print(b)
for i in range(0,8):
    c=a+b
    print(c)
    a=b
    b=c
'''    
#abs is a function  means modulus for converting into positive
#NEW TOPIC : LIST IN PYTHON(IN JAVA CALLED ARRAYLIST)
#APPEND ADDS ONLY ONE ELEMENT IN THE LIST WE CAN ADD MORE BY TAKE IT IN LOOP
'''
l=[]
a=list()
num=int(input("NUMBER: "))
a.append(num)
print(a)
'''
'''
a=list()
for i in range(5):
    num=int(input("enter your number: "))
    a.append(num)
print(a)
a.insert(3,66)
print(a)
'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
#l3=l1+l2
#print(l3)
#l4=l1*2
#print(l4)
l1.extend(l2)
print(l1)
















    
    
    
    