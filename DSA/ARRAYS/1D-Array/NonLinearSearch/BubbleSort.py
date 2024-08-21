#code of bubble sort
def BubbleSort(A,l):
    for i in range(1,l,1):
        for j in range(0,l-i,1):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
#insertion in a sorted Array
def insertSort(A,num):
    # for i in range(0,l,1):
    #     if(A[i]<num and A[i+1]>num):
    #         A[l+1] = A[l]
    #         num=A[i+1]
    k=0
    while k < len(A) and A[k] < num:
        k += 1
    B= A[:k] + [num] + A[k:]
    print(B)

    return B

    
A=[90,80,70,60,50,40,30,20,10]
l=len(A)
BubbleSort(A,l)
for x in range(l):
    print(A[x])

num=int(input('Enter the number: '))
B=insertSort(A,num)
print(B)




    

            
