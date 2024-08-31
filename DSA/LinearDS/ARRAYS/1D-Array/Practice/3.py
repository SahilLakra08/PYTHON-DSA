# 3. Finding the Maximum Value in a List
# •Question: Write a Python function find_max(lst) that 
# returns the maximum value in a list using a linear search method.

def find_max(lst):
    l=len(lst)
    max1=0
    for i in range(0,l):
        if(max1<lst[i]):
            max1=lst[i]
    return max1

lst=[1,2,3,4,5,6,7,8]
result=find_max(lst)
print('Maximum Value in the list is :',result)
