def input_matrix(A, m, n):
    for i in range(m):
        for j in range(n):
            A[i][j] = int(input(f'Enter the element at position ({i},{j}): '))

def addmatrix(A, B, C, m, n):
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

def display(matrix):
    for row in matrix:
        print(row)

m = 2
n = 3
A = [[0 for j in range(n)] for i in range(m)]
input_matrix(A, m, n)
print("Matrix A:")
display(A)

o = 2
p = 3
B = [[0 for j in range(p)] for i in range(o)]
input_matrix(B, o, p)
print("Matrix B:")
display(B)

# Initialize C with the correct dimensions
C = [[0 for j in range(n)] for i in range(m)]

# Add matrices A and B
addmatrix(A, B, C, m, n)

print("Matrix C (A + B):")
display(C)
