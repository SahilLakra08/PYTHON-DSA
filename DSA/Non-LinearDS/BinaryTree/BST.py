# Binary Search Tree :
#binary search tree creation
# no duplicate element in BST
class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def insert1(root,num):
    if root == None:     
        root=node(num)
        root.left=None
        root.right=None

    elif num < root.data:
        root.left = insert1(root.left,num)  

    elif (num > root.data):
        root.right = insert1(root.right,num)
    else:
         print('Duplicate element not allowed.')
    return root
    
def search(root,key):
     if(root is None):
          return False
     elif (root.data == key):
          return True
     elif (key> root.data):
            return search(root.right,key)
     else:
            return search(root.left,key)
     
     #check the tree is binary tree or not.
def isBSt(root,min1,max1):
    if root == None:
        return True
    elif (root.data > max1) or (root.data < min1):
         return False
    else:
         return isBSt(root.left , min1,root.data) and isBSt(root.right,root.data,max1)
        
def countnodes(root):
    if root is None:
        return 0 
    else:
         p= countnodes(root.left)
         q= countnodes(root.right)
         return 1+p+q
     
def inorder(root):
        if root == None:
              return 
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

def preorder(root):
      if root == None:
            return
      else:
            print(root.data)
            preorder(root.left)
            preorder(root.right)

def postorder(root):
      if root == None:
            return
      else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)
           
root = None
nodes = int(input('enter the number of nodes : '))
for i in range(nodes):
    num =int(input('Enter the root : '))
    root=insert1(root,num)

print('',end='->')
print('INORDER TRAVERSAL : ')
inorder(root)
# print('',end='->')
# print('PREORDER TRAVERSAL : ')
# preorder(root)
# print('',end='->')
# print('POSTORDER TRAVERSAL : ')
# postorder(root)


# #search
# key = int(input('Enter the element to be searched : '))
# x = search(root,key)
# print(x)

#count
# y=countnodes(root)
# print('Size of tree: ',y)
#check isBSt
min1 = 0
max1 = 100
i = isBSt(root,min1,max1)
print(i)

# DEFINITIONS:
# root
# edges
# nodes
# leaf nodes
# child nodes
# parent node
# height
# size

# balanced tree : height difference 1
# full tree : 0 or 2 nodes
# perfect tree : balanced tree + full tree

# do merge sort in sorted array ? 