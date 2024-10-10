# to add all elements of array

def sum1(A,l):
    if l == -1:
        return 0
    else:
        return A[l]+sum1(A,l-1)

    
A = [1,2,3,4,5]
l=len(A) 
a=sum1(A,l-1)
print(a)

# check whether a given string is pallindrome or not using recursion