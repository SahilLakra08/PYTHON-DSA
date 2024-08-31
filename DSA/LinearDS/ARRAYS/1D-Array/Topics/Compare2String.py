def compare2Strings(lst,l):
    for i in range(1,l):
        for j in range(0,l-i):
            if lst[j]>lst[j+1]:
                 lst[j],lst[j+1]=lst[j+1],lst[j]


lst=['Sahil','Akshat','Sagar','Sourav','Aalok','lakra']
l=len(lst)
compare2Strings(lst,l)
print(lst)