# def reverse(A,l,i):
#     if i == l :
#         return 0
#     else :
#         print(A[i])
#         reverse(A,l,i+1)

def reverse(A,l,i):
    if i == 0 :
        return 0
    else :
        print(A[i-1])
        reverse(A,l,i-1)

A=[1,2,3,4,5]
l=len(A)
i=l
reverse(A,l,i)
