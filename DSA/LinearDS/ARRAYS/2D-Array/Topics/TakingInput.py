m=int(input('Enter No. of rows:'))
n=int(input('Enter No. of columns:'))
A= [ [0 for j in range (n)]for i in range (m)]
for i in range (m):
    for j in range (n):
        A[i][j]=int(input('Enter the elements of the Matrix:'))
        
for i in range(m):
    for j in range(n):
        print(A[i][j],end=' ')
    print('')

# print(A)