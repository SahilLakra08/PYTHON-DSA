#Given a list in Python and provided the positions of the elements,
#write a program to swap the two elements in the list. 
def swap(L,l,x,y):
    L[x],L[y]=L[y],L[x]
    print(L)


L=[10,20,30,40,50,60,70,80]
l=len(L)
x=int(input('Enter the index number: '))
y=int(input('Enter the index number you want to change it with: '))
swap(L,l,x,y)
