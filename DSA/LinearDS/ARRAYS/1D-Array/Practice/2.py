# 2. Linear Search for Multiple Occurrences
# •Question: Modify the linear_search function to return a list of all indices 
# where the target appears in the list. If the target is not found, return an empty list.
def linear_search(lst,target):
    indexList=[]
    for i in range(0,l):
        if(lst[i]==target):
            indexList.append(i)
    return indexList

lst=[1,2,1,2,3,4,4,5,6,8,8,87,6,7,8,9]
l=len(lst)
target=int(input('Enter the number: '))
result=linear_search(lst,target)
print('index of target in list :',result)
