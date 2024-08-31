def MaxMin(A,l):
    max1=0
    min1=A[0]
    for i in range(1,l,1):
        if(max1<A[i]):
            max1=A[i]
   
        elif(A[i]<min1):
            min1=A[i]
    return max1,min1
A=[1,2,3,4,55,33,77,58]
l=len(A)
x,y=MaxMin(A,l)
print(x,y)