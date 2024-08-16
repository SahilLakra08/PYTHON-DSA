l1=[10,20,10,30,40,50,30]
for i in l1:
    if l1.count(i)>1:
        l1.remove(i)
print(l1)