def binsearch(A,num,lb,ub):
    if lb > ub:
        return -1
    else:
        mid =(lb+ub)//2
        if A[mid]==num :
            return mid
        elif (num>A[mid]):
            return binsearch(A,num,mid+1,ub)
        elif (num<A[mid]):
            return binsearch(A,num,lb,mid-1)
            
A=[10,20,30,40,50,60,70,80,90,100]
l=len(A)
lb=0
ub=l-1
num=int(input('Enter the number you want to search: '))
a=binsearch(A,num,lb,ub)
if a == -1:
    print('Element doesnt exists.')
else:
    print('Element exists.')