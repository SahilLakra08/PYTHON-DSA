def Create(n):
    if n % 2 == 0:
        print('Invalid! Please Enter Only Odd Dimensions .')
    else:
        A = [[0 for i in range(n)] for j in range(n)]
        k = 1
        mid = n // 2
        A[0][mid] = k
        i = 0
        j = mid
        while k < n * n:
            k += 1
            i -= 1
            j += 1

            if i < 0:
                i = n - 1
            if j > n - 1:
                j = 0

            if A[i][j] != 0:
                i += 2
                j -= 1

            if i >= n:  # Ensure i is within bounds after collision correction
                i = 0
            if j < 0:   # Ensure j is within bounds after collision correction
                j = n - 1

            A[i][j] = k

        for row in A:
            print(row)

n = int(input('Enter the Dimension for Magic Square: '))
Create(n)
