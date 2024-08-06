L1=["Apple","Grapes","Guava","Banana","Leeche"]
print(sorted(L1,reverse=True))#for descending order
#for ascending order
print(sorted(L1))
print(sorted(L1,reverse=False))
#for deleting element in list
L1.pop()
print(L1)
L1.pop(3)
print(L1)
#for deleting the whole list
#del(L1)
#print(L1)
#'.remove' is also used to remove particular element from the list
L1.remove("Apple")
print(L1)

L2=[1,2,45,65,3,23,65,323]
x=L2.count(65)
print(x)
y=L2.index(3)
print(y)