#unpacking a list or string into another list
str1="HELLO SAHIL "
L=[*str1]
print(L)
L1=[1,2,3]
Lfinal=[4,5,*L1,6]
print(Lfinal)
L2=["SAHIL","AKSHAT","SAGAR","SOURAV","AALOK"]
L2[1]="ROY"
print(L2)
L2.insert(2,"LAKRA")
print(L2)
L2.remove("ROY")
print(L2)
x=L2.index("SAHIL")
print(x)
L3=["Apple","Guava","Mango","POMEgranate"]
L3.reverse()
print(L3)
L3.sort()
print(L3)

str2="LAKRA"
l=list(str2)
print(l)