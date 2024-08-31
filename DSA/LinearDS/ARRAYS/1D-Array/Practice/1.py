# 1. Basic Linear Search
#Question: Write a Python function linear_search(lst, target) 
#  that takes a list lst and a target value as input. 
#The function should return the index of the target 
# in the list if found, otherwise return -1.

def linear_search(lst,target):
     l=len(lst)
     for i in range(0,l):
          if(lst[i]==target):
               return i
     return -1  
            
   
lst=[1,2,3,4,5,6,7,8,9]
target=int(input('Enter the number: '))
result=linear_search(lst,target)
print('index of target in the list is : ',result)