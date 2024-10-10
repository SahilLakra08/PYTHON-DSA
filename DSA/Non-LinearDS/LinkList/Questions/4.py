# INSERTION IN SORTED LINKED LIST :

class node:
    def __init__(self,d):
        self.data=d
        self.link= None 
def create():
    global start
    choice = 'y'
    d= int(input('enter the first element : '))
    start = node(d)
    start.data = d
    start.link = None
    ptr=start
    while(choice == 'y' or choice == 'Y'):
        d= int(input('enter the element : '))
        q = node(d)
        q.data = d
        q.link = None
        ptr.link=q
        ptr= ptr.link
        choice = input('Do you want to continue Y/N :')
        
def insertion1():
    global start
    ptr=start
    num=int(input('Enter the element you want to insert: '))
    q=node(num)
    q.data=num
    if start.data >num:
        q.link = start
        start = q
    else:
        while(ptr.link is not None ):
            if(ptr.link.data>num):
                q.link=ptr.link
                ptr.link =q
                break
            else:
                ptr=ptr.link
        
def display1():
    global start
    ptr = start 
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.link  

start=None
create()
display1()
insertion1()
display1()
