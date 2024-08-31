#  Checking if a List is Sorted
# •	Question: Write a Python function is_sorted(lst) 
# that checks whether a list is sorted in non-decreasing order 
# using a linear search approach.


def is_sorted(lst,l):
    if(l<2):
        return True
    for i in range(l):
        if(lst[i]>lst[i+1]):
            return False
        else: return True

lst=[9,8,7,6,5,4,3,2,1]
# lst=[1,2,3,4,5,6,7,8,9]
l=len(lst)
print(is_sorted(lst,l))