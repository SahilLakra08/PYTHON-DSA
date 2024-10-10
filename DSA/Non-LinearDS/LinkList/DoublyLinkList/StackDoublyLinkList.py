class node:
    def __init__(self,d):
        self.data = d
        self.previous = None
        self.next = None

class doublylinklist:
    def __init__(self):
        self.top = None
        # self.top.previous = None
        # self.top.next = None
        
    def push1(self):
        data=int(input('Enter the element you want to enter on top: '))
        q=node(data)
        if self.top is None:    
            self.top = q
        else:  
            q.next = self.top
            self.top.previous = q
            self.top = q

    def InsertAfterNum(self,num):
        #insert after number
        self.ptr = self.top
        while(self.ptr.data != num):
            self.ptr = self.ptr.next
        data=int(input('Enter the element you want to insert after1 : '))
        q = node(data)
        q.next = self.ptr.next
        self.ptr.next = q

    def pop1(self):
        # for Detachment:
        # self.ptr = self.top
        # self.ptr.next= None
        self.top = self.top.next
        self.top.previous = None
        
    def display1(self):
        self.ptr=self.top
        while self.ptr!=None:
            print(self.ptr.data , end="->")
            self.ptr= self.ptr.next

    def display2(self):
        # Moving Pointer To End
        self.ptr = self.top
        while(self.ptr.next != None):
            self.ptr = self.ptr.next
        # BackTraversing
        self.q = self.ptr
        while(self.q != None):
            print(self.q.data , end="->")
            self.q = self.q.previous

st=doublylinklist()
while(True):
    print('    DOUBLY LINKED STACK OPERATION      ')
    print('         1.PUSH      ')
    print('         2.POP       ')
    print('         3.Display Forward       ')
    print('         4.Display Backward       ')
    print('         5.EXIT       ')
    print('         6.Insert After           ')

    choice=int(input('Enter your choice: '))

    if choice == 1:
        st.push1()

    elif choice == 2:
        st.pop1()

    elif choice == 3:
        st.display1()

    elif choice == 4:
        st.display2()

    elif choice == 5:
        exit(0)
    elif choice == 6:
        num=int(input('Enter Number to be searched in last:'))
        st.InsertAfterNum(num)
    else :
        print('Wrong Choice')

# st.push1()
# st.push1()
# st.push1()
# st.pop1()
# st.pop1()
# st.display()


        



























