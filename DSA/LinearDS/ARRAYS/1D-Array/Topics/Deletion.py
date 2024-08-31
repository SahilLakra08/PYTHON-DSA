def Delete_k(A,l,k):
    A[k:l-1]=A[k+1:l]


A=[1,2,3,45,54,34,65,23,54]
#physical deletion is not possible in Array
#without del function we cannot delete element in the array 
#here we are just shifting the elements in the array
k=int(input('Enter the index to delete: '))
l=len(A)
Delete_k(A,l,k)
l=l-1
for i in range(l):
    print(A[i])



