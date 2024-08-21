#program to count how many number of times the number is repeating in the array
def count(A,l,num):
    count=0
    for i in range(0,l):
        if(A[i]==num):
            count=count+1
    return count

A=[1,2,3,4,5,8,6,8,6,8,8,9,8]
l=len(A)
#num=8
num=int(input('Enter the Number: '))
Count=count(A,l,num)
if(Count!=0):
    print('Repetion is: ',Count,'times')
else:
    print('No Repetition')