# a=1
# b=4
# print (a+b)

# L=[1,2,3,4,5,6,7,8,9,0,0,0]
# L[2]=L[3]
# print(L)


# #insert new element in the array with given index and number with no repetition.
# def insert(L,k,num,l):
#     for i in range(l-1,k-1,-1):
#         L[i]=L[i+1] #step for shifting down
#     L[k]=num #insertion step

# L=[1,2,3,4,5,6,7,8,9]
# l=len(L)
# k=int(input('Enter the Index Number: '))
# num=int(input('Enter the number you want to insert: '))
# insert(L,k,num,l)
# print(L)

def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def insertSort(A, num):
    # Find the correct position to insert the new number
    k = 0
    while k < len(A) and A[k] < num:
        k += 1
    
    # Insert the new number into the correct position using slicing
    A = A[:k] + [num] + A[k:]
    return A

# Initial array
A = [90, 80, 70, 60, 50, 40, 30, 20, 10]

# Sort the array
BubbleSort(A)
print("Sorted array:")
print(A)

# Input number to be inserted
num = int(input('Enter the number: '))

# Insert the number into the sorted array
A = insertSort(A, num)

# Print the array after insertion
print("Array after insertion:")
print(A)
