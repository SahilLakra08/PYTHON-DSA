def BinarySearch(A,l,num):
    lb=0
    ub=l-1
    while(lb<=ub):
        #1
        mid=(lb+ub)//2
        #2
        if(A[mid]==num):
            print('Search Successful')
            exit(0) # to end the loop.
        #3
        elif(num>A[mid]):
            lb=mid+1
            ub=l-1
            mid=(lb+ub)//2
        #4
        elif(num<A[mid]):
            ub=mid-1
            mid=(lb+ub)//2
    print('Element does not exists')

A=[10,20,30,40,50,60,70,80,90,100]
l=len(A)
num=int(input('Enter the number you want to search: '))
BinarySearch(A,l,num)
