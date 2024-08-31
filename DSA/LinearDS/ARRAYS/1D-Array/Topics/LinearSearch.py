#Searching element in the array or list


def LinearSearch(A,l,num):
    flag=0
    for i in range(0,l):
        if(A[i]==num):
            flag=1
            break
    return flag
    

A=[1,2,3,4,5,6,7,8,9]
l=len(A)
num=5
found=LinearSearch(A,l,num)
if(found):
    print('Number Found')
else:
    print('Search UnsuccessFul')




    
