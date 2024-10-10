# creation of linked queue
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
def display():
    global start
    ptr = start 
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.link

create()

display()
