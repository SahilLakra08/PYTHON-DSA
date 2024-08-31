def InsertionSort(lst,l):
    lst[0]=-32768
    for k in range(1,l):
        temp=lst[k]
        ptr=k-1
        while(lst[ptr]>temp):
            lst[ptr+1]=lst[ptr]
            ptr=ptr-1
        lst[ptr+1]=temp
    
lst=[32,54,58,78,89,76,123,99,1]
l=len(lst)
InsertionSort(lst,l)
print(lst[1:l])
