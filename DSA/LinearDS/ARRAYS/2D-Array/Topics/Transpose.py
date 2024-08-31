
def input_matrix(A, m, n):
    # Initialize the matrix A with zeros
    A = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            A[i][j] = int(input('Enter the element of matrix: '))
    return A

def transpose(A, B, m, n):
    # Initialize B with the transposed dimensions
    B = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    return B

m = 2
n = 3

# Initialize matrix A
A = [[0 for j in range(n)] for i in range(m)]
A = input_matrix(A, m, n)  # Correctly populate matrix A
print("Matrix A:")
for row in A:
    print(row)

# Initialize matrix B
B = [[0 for j in range(m)] for i in range(n)]
B = transpose(A, B, m, n)  # Correctly populate matrix B with the transpose of A
print("Matrix B (Transpose of A):")
for row in B:
    print(row)

