#  MERGING OF 2 LINKED LIST
class node:
    def __init__(self,d):
        self.data=d
        self.link= None

class LinkedList:
    def __init__(self):
        self.top1 = None
        self.top2 = None
        self.q=None

    def push1(self): 
            data=input('enter the element to be inserted: ')
            self.q=node(data)
            self.q.link=self.top1
            self.top1=self.q
    def push2(self): 
            data=input('enter the element to be inserted: ')
            self.q=node(data)
            self.q.link=self.top2
            self.top2=self.q

    #function for merge
    def merge1(self):
        self.ptr = self.top1
        while(self.ptr.link != None):
             self.ptr = self.ptr.link       
        self.ptr.link = self.top2
            
    def display1(self):
            self.p=node(0)
            self.p=self.top1
            while(self.p is not None):
                 print(self.p.data, end="->")
                 self.p = self.p.link
        
# Main :
st= LinkedList()

while(True):
    print('     STACK OPERATION      ')
    print('         1.PUSH1      ')
    print('         2.PUSH2       ')
    print('         3.MERGING       ')
    print('         4.DISPLAY       ')
    print('         5.EXIT       ')

    choice=int(input('Enter your choice: '))


    if choice == 1:
        st.push1()

    elif choice == 2:
        st.push2()

    elif choice == 3:
        st.merge1()

    elif choice == 4:
        st.display1()

    elif choice == 5:
        exit(0)
    else :
        print('Wrong Choice')











