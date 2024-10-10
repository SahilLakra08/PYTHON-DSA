class node:
    def __init__(self,d):
        self.data=d
        self.link= None
class LinkedList:
    def __init__(self):
        self.front = None
        self.rear=None

    def enqueue(self):
        data=int(input('enter the element to enqueue: '))
        self.q=node(data)
        
        if(self.front==None and self.rear == None):
            self.front = self.q
            self.rear = self.q
        else:
            self.rear.link = self.q
            self.rear = self.rear.link

    def dequeue(self):
        if self.front == None :
            print('Queue is empty')
        else :
            self.ptr=self.front
            self.front = self.front.link
            self.ptr=None
            # self.p.link = None #detach 1rst node from linked queue

    def display(self):
        self.p = self.front
        print(self.front)
        while(self.p is not None ):
            print(self.p.data, end = '->' )
            self.p=self.p.link

st=LinkedList()
front = None
rear = None
# st.enqueue()
# st.enqueue()
# st.dequeue()
# st.display()

while(True):
    print('     QUEUE OPERATION      ')
    print('         1.ENQUEUE      ')
    print('         2.DEQUEUE       ')
    print('         3.DISPLAY       ')
    print('         4.EXIT       ')

    choice=int(input('Enter your choice: '))

    if choice == 1:
        st.enqueue()

    elif choice == 2:
        st.dequeue()

    elif choice == 3:
        st.display()

    elif choice == 4:
        print(' Thank You !!! ')
        exit(0)
    else :
        print('Wrong Choice')