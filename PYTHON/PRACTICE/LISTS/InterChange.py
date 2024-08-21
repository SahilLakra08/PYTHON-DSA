#Python program to interchange first and last elements in a list

def InterChange(L,l):
    L[0],L[l-1]=L[l-1],L[0]
    print(L)

L=[10,20,30,40,50,60,70,80]
l=len(L)
InterChange(L,l)

