class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

root=node(10)
def create1(root):
        # print(root.data)
      #   root.left = node(12)
      #   root.left.left = node(15)
      #   root.left.left.left = None
      #   root.left.right = node(20)
      #   root.right = node(17)

#for bst function data is :
        root.left = node(8)
        root.left.left = node(2)
        root.left.right = node(9)
        root.right = node(12)
        root.right.left = node(11)
        
# inorder ---> left -> node -> right
def inorder(root):
        if root == None:
              return 
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

# preorder ---> node -> left -> right
def preorder(root):
      if root == None:
            return
      else:
            print(root.data)
            preorder(root.left)
            preorder(root.right)

# postorder ---> left -> right -> node
def postorder(root):
      if root == None:
            return
      else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)

def isBSt(root,min1,max1):
    if root == None:
        return True
    elif (root.data > max1) or (root.data < min1):
         return False
    else:
         return isBSt(root.left , min1,root.data) and isBSt(root.right,root.data,max1)
        

create1(root)
inorder(root)
print('',end='->')
min1 = 0
max1 = 100
i = isBSt(root,min1,max1)
print(i)
# preorder(root)
# print('',end='->')
# postorder(root)
