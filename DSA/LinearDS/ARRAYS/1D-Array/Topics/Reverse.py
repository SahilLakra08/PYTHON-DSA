# A=[20,21,22,23,24,25]
#copy contents of A into array B in reverse order

def reverse(A,l):
    B = [ 0  for i in range (l)]
    for i in range (l):
        B[i]= A[l-1-i]
    print(B)


A = [20,21,22,23,24,25]
l=len(A)
reverse(A,l)