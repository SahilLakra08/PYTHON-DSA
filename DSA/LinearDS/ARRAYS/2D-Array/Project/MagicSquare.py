def generate_Square(n): 
    # 2-D array with all slots set to 0 

    magicSquare = [[0 for x in range(n)] 
                      for y in range(n)] 
    # initialize position of 1 
    i = n / 2
    j = n - 1
    # Fill the square by placing values 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n: # condition 3
            j = n - 2
            i = 0
        else:  
            # next number goes out of 
            # right side of square  
            if j == n: 
                j = 0    
            # next number goes  
            # out of upper side 
            if i < 0: 
                i = n - 1
        if magicSquare[int(i)][int(j)]: #condition 2
            j = j - 2
            i = i + 1
            continue
        else: 
            magicSquare[int(i)][int(j)] = num 
            num = num + 1
        j = j + 1
        i = i - 1 # condition 1
    # Printing the square 
    print ("Magic Square for n =", n) 
    print ("Sum of each row or column",n * (n * n + 1) / 2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (magicSquare[i][j]),end = '') 
            # To display output  
            # in matrix form 
            if j == n - 1:  
                print()


n=int(input("Number of rows of the Magic Square:"))
generate_Square(n)