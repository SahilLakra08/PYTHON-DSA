def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row to set the target sum
    target_sum = sum(matrix[0])
    
    # Check all rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check all columns
    for col in range(n):
        column_sum = 0
        for row in range(n):
            column_sum += matrix[row][col]
        if column_sum != target_sum:
            return False
    
    # Check the main diagonal
    main_diagonal_sum = 0
    for i in range(n):
        main_diagonal_sum += matrix[i][i]
    if main_diagonal_sum != target_sum:
        return False
    
    # Check the anti-diagonal
    anti_diagonal_sum = 0
    for i in range(n):
        anti_diagonal_sum += matrix[i][n - 1 - i]
    if anti_diagonal_sum != target_sum:
        return False
    
    return True

# Take matrix input from the user
n = int(input("Enter the size of the matrix (n x n): "))
matrix = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check if the matrix is a magic square
if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")

