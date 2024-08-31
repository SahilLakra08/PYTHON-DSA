# # 2-D array: is collection of rows and column
# syntax for nested list in 2-D array is :
#         L=[[]]


#new topic- List comprehension
lst=[[0 for j in range(3)]for i in range(4)]


for i in range(0,4):
    for j in range(0,3):
        lst[i][j]=i+j
        print(i+j,end=' ')
    print('')

#give contents of lst[i][j]

print(lst)
print(lst[1][2])