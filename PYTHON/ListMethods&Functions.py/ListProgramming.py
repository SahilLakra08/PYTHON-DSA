#LIST HAS TWO TYPES OF FUNCTIONS OR METHODS
'''
 1.len(l1)                           1. .count() element which comes the most (searching)
2.max(l1)                           2. .index() tells the index element(searching)
3.min(l1)                           3. .sort()
4.sum()                             4. .reverse()
5.any()                             5. 
6.all()                             6.
7.del()                             7.
8.sorted()                          8.
9.reversed()                        9.
reversed m hum likte hai           10.
print(list(reversed(listName))) 
'''


L1=["Apple","Guava","Mango","POMEgranate"]

L1.append("Grapes")
L1.insert(0,"Pear")
L2=["Pineapple","Leechi"]
L1.extend(L2)
print(L1)
L3=L1+L2
#USED TO CHECK WHICH CLASS BELONGS TO:
print(type(L1))
print(len(L1))
print(sorted(L1))
l4=[2,4,5,3,1,5]
print(list(reversed(l4)))
print(sorted(L1,reverse=T))
transport=[True,False,False,True,True]
print(any(transport))
print(all(transport))
L1.pop()
print(L1)
L1.pop(3)
print(L1)

a=[1,3,5,7,9]
print(sum(a))
