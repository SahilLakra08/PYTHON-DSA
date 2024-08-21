#Write a program to print the following number pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()