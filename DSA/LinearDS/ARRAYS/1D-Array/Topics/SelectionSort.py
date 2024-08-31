# def SelectionSort(A,l):
#     for i in range(0,l-1,1):
#         for j in range(i+1,l,1):
#             if(A[i]>A[j]):
#                 A[i],A[j]=A[j],A[i]
#     # print(A)


# MORE EFFICIENT WAY IN SELECTION SORT:

def SelectionSort(A,l):
    for i in range (0,l-1,1):
        minpos=i
        for j in range (i+1,l-1,1):
            if(A[j]<A[minpos]):
                minpos=j
        A[i],A[minpos]=A[minpos],A[i]
                


A=[93,37,84,25,13,9,546]
l=len(A)
SelectionSort(A,l)
print(A)