# . Removing Duplicates from a List
# •	Question: Write a Python function remove_duplicates(lst) 
# that returns a new list with duplicates removed, maintaining the original order.

# DOUBT!!!!!!!!!!!!!!

# def remove_duplicates(lst):
#     l=len(lst)
#     new=[]
#     for i in range (l):
#         if(lst.count>1):
#             lst.remove
#     new[i]=lst[i]
#     return new[i]
            


# lst=[1,2,3,4,2,3,5,6,5,6,8,9,8,7,8]
# print(lst)
# print(remove_duplicates(lst))
def remove_duplicates(lst):
    new = []  # List to store the result
    for i in range(len(lst)):
        if lst[i] not in new:
            new.append(lst[i])
    return new

# Example usage
lst = [1, 2, 3, 4, 2, 3, 5, 6, 5, 6, 8, 9, 8, 7, 8]
print("Original list:", lst)
print("List with duplicates removed:", remove_duplicates(lst))
