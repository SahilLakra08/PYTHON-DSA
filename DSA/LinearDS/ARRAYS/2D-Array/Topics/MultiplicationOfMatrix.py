def input_matrix(A,m,n):
    for i in range(m):
        for j in range(n):
            A[i][j]=int(input('Enter the element in matrix 1 at position({i},{j}): '))

def multiply_matrix(A,B,C,m,n,o,p):
    for i in range(m):
        for j in range(p):
            C[i][j] = 0
            for k in range(0,n):
                C[i][j]=C[i][j]+A[i][k] * B[k][j]

def display(matrix,x,y):
    for i in range(x):
        for j in range(y):
            print(matrix[i][j],end='   ')
        print()

m = 3
n = 4
A=[[0 for j in range(n)]for i in range(m)]
input_matrix(A,m,n)
print('Matrix A: ')
display(A,m,n)

o = 4
p = 3
B=[[0 for j in range(p)]for i in range(o)]
input_matrix(B,o,p)
print('Matrix B: ')
display(B,o,p)

C=[[0 for j in range(m)]for i in range(p)]
multiply_matrix(A,B,C,m,n,o,p)
print('Matrix C(A*B): ')
display(C,m,p)




# GENERAL CODE FOR MULTIPLICATION OF THE MATRIX 
# TO CHECK THE DIMENSIONS AND CONDITIONS FOR CHECKING THE MULTIPLICATION IS POSSIBLE OR NOT .


# def input_matrix(A, m, n):
#     for i in range(m):
#         for j in range(n):
#             A[i][j] = int(input(f'Enter the element in matrix at position ({i}, {j}): '))

# def multiply_matrix(A, B, C, m, n, o, p):
#     for i in range(m):
#         for j in range(p):
#             C[i][j] = 0
#             for k in range(n):  # Assuming n == o for valid matrix multiplication
#                 C[i][j] += A[i][k] * B[k][j]

# def display(matrix, x, y):
#     for i in range(x):
#         for j in range(y):
#             print(f'{matrix[i][j]:4}', end=' ')  # Adjusted spacing for better readability
#         print()

# def can_multiply(n, o):
#     return n == o

# # Get dimensions from the user for matrix A (m x n)
# m = int(input("Enter the number of rows for Matrix A: "))
# n = int(input("Enter the number of columns for Matrix A (and rows for Matrix B): "))

# A = [[0 for j in range(n)] for i in range(m)]
# print('Enter elements for Matrix A:')
# input_matrix(A, m, n)
# print('Matrix A:')
# display(A, m, n)

# # Get dimensions from the user for matrix B (o x p)
# o = n  # Ensure o matches n from Matrix A
# p = int(input("Enter the number of columns for Matrix B: "))

# B = [[0 for j in range(p)] for i in range(o)]
# print('Enter elements for Matrix B:')
# input_matrix(B, o, p)
# print('Matrix B:')
# display(B, o, p)

# # Check if multiplication is possible
# if can_multiply(n, o):
#     # Initialize result matrix C (m x p)
#     C = [[0 for j in range(p)] for i in range(m)]

#     # Multiply matrices
#     multiply_matrix(A, B, C, m, n, o, p)
#     print('Matrix C (A * B):')
#     display(C, m, p)
# else:
#     print("Matrix multiplication is not possible. The number of columns in Matrix A must be equal to the number of rows in Matrix B.")
