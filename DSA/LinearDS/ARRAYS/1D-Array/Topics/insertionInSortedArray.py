
# def insertSort(A,l,num):
#     k =0
#     for i in range(l):
#         if(A[i]>num):
#             k=i
#             break
#         else : continue
    
#     for j in range(l-1,k-1,-1):
#         A[j+1]=A[j]
#     A[k]=num

    
# A=[13,54,67,89,90,99]
# l=len(A)-1
# num =int(input('Enter the Element: '))
# insertSort(A,l,num)
# for p in range(l+1):
#     print(A[p])

    
def insertSort(A,l,num):
    k =0
    for i in range(l):
        if(A[i]>num):
            k=i
            break
        else : continue
    
    for j in range(l-1,k-1,-1):
        A[j+1:]=A[j:]
    A[k]=num

    
A=[13,54,67,89,90,99]
l=len(A)-1
num =int(input('Enter the Element: '))
insertSort(A,l,num)
for p in range(l+1):
    print(A[p])