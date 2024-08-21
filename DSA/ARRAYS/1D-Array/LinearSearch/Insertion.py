#insert new element in the array with given index and number with no repetition.
def insert(L,k,num,l):
    #for i in range(l-1,k-1,-1):
    #    L[i+1]=L[i] #step for shifting down
    L[k+1:l+1] = L[k:l:1]
    L[k]=num #insertion step

L=[1,2,3,4,5,6,7,8,9,0,0,0]
l=len(L)
k=int(input('Enter the Index Number: '))
num=int(input('Enter the number you want to insert: '))
insert(L,k,num,l)
print(L)