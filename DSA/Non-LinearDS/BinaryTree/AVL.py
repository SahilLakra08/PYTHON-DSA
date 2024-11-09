class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
        self.height = None
    
def getHeight(root):
     if root is None:
          return -1
     else:
        #   root.height = 1+max(getHeight(root.left),getHeight(root.right))
        #   return root.height 

        x= getHeight(root.left)
        y = getHeight(root.right)
        return 1 + max(x,y)

def getBalance(root):
     if root is None:
          return 0
     else:
          balance = getHeight(root.left) - getHeight(root.right)
          return balance
     
#check the tree is binary tree or not.
def isBSt(root,min1,max1):
    if root == None:
        return True
    elif (root.data > max1) or (root.data < min1):
         return False
    else:
         return isBSt(root.left , min1,root.data) and isBSt(root.right,root.data,max1)

def inorder(root):
        if root == None:
              return 
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

def rightRotate(y):
     # y = root
     x = y.left
     t2= x.right

    # Switching or assigning values for rotation
     x.right=y
     y.left=t2

    #updating height
     # root.height =  1+max(getHeight(x.left),getHeight(y.right))
     # return x    

    #   # Update heights after rotation
     a = 1 + max(getHeight(y.left), getHeight(y.right))  
     b = 1 + max(getHeight(x.left), getHeight(x.right))  

    # Return the new root (x)
     return x
def leftRotate(x):
     # x = root
     y= x.right
     t2 = y.left
     # Switching or assigning values for rotation
     y.left=x
     x.right=t2

     #updating height
     # root.height =  1+max(getHeight(x.left),getHeight(y.right))
     a = 1 + max(getHeight(y.left), getHeight(y.right))  
     b = 1 + max(getHeight(x.left), getHeight(x.right))  
     balance = getHeight(root.left) - getHeight(root.right)
     # new root
     return y

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
   # return root
    
    # Modify insert function to keep updating height of BST
    #root.height =  1+max(getHeight(root.left) - getHeight(root.right))

    #also getBalance factor
    balance = getHeight(root.left) - getHeight(root.right)
    
    #check all the cases LL , RR , LR , RL

    #for LL Imbalance(Right Rotate)
    if(balance>1)and (num < root.left.data):
         return rightRotate(root)
         
    # for RR Imbalance (Left Rotate)
    elif (balance<-1)and (num>root.right.data):
         return leftRotate(root)
    
    # for LR Imbalance(Left-right rotate)
    elif(balance>1)and (num>root.left.data):
         root.left = leftRotate(root.left)
         return rightRotate(root)
    
    # for RL Imbalance(Right-Left rotate)
    elif(balance<-1) and (num<root.right.data):
         root.right=rightRotate(root.right)
         return leftRotate(root)

    return root

# do word count or number count or word and number frequence
# insertion           
root = None
nodes = int(input('enter the number of nodes : '))
for i in range(nodes):
    num =int(input('Enter the root : '))
    root=insert1(root,num)

print('',end='->')
print('INORDER TRAVERSAL : ')
inorder(root)

#check isBSt
min1 = 0
max1 = 100
i = isBSt(root,min1,max1)
print(i)

#get Height
j = getHeight(root)
print('Height : ',j)

# get balance
balance = 0
k = getBalance(root) 
print("Balance: ",k)

