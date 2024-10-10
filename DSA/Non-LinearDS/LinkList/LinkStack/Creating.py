class node:
    def __init__(self,d):
        self.data=d
        self.link= None
class LinkedList:
    def __init__(self):
        self.top = None
        self.q=None
    # TO PRINT ALTERNATE ELEMENTS
    def print1(self):
        self.ptr = self.top
        while(self.ptr != None and self.ptr.link != None):
            print(self.ptr.data ,end= "->")
            self.ptr = self.ptr.link.link
            
    def push1(self): 
            data=int(input('enter the element to be inserted: '))
            self.q=node(data)
            self.q.link=self.top
            self.top=self.q

    def pop1(self):
            if self.top ==None :
                print('Stack is Empty')
            else:
                 self.top = self.top.link

    def peek1(self):
        if self.top == None:
             print('Stack is Empty')
        else:
            print(self.top.data)

    def display1(self):
            self.p=node(0)
            self.p=self.top
            while(self.p is not None):
                 print(self.p.data, end="->")
                 self.p = self.p.link
        
# Main :
st= LinkedList()

while(True):
    print('     STACK OPERATION      ')
    print('         1.PUSH      ')
    print('         2.POP       ')
    print('         3.PEEK       ')
    print('         4.DISPLAY       ')
    print('         5.Print ALternate       ')
    print('         6.EXIT       ')

    choice=int(input('Enter your choice: '))


    if choice == 1:
        st.push1()

    elif choice == 2:
        st.pop1()

    elif choice == 3:
        st.peek1()

    elif choice == 4:
        st.display1()

    elif choice == 5:
        st.print1()
    elif choice == 6:
        exit(0)
    else :
        print('Wrong Choice')





# #PROJECT: THERE IS A PARKING LOT JISMAI GAADIYAN STACK MAI LGANI HAI 
# CLASS BNAGI CAR KE NAME se
# DATA ADD HOGA STRING MEANS CAR NUMBER



