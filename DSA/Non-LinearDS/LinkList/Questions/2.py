# INSERTION IN A LINKED LIST
# AFTER  Kth POSITION

class node:
    def __init__(self,d):
        self.data=d
        self.link= None
class LinkedList:
    def __init__(self):
        self.top = None
        self.q=None

    def push1(self): 
            data=int(input('enter the element to be inserted: '))
            self.q=node(data)
            self.q.link=self.top
            self.top=self.q

    def insertafter(self,num):
         self.ptr = self.top
         count = 1
         while(self.ptr != None and count < num):
              self.ptr = self.ptr.link
              count = count+1
         if self.ptr == None:
              print('POSITION doesnt exists.')
         else:
              data =int(input('Enter the number: '))
              q = node(data)
              q.link = self.ptr.link
              self.ptr.link = q

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
    print('         2.INSERT_AFTER       ')
    print('         3.DISPLAY       ')
    print('         4.EXIT       ')

    choice=int(input('Enter your choice: '))

    if choice == 1:
        st.push1()

    elif choice == 2:
        num=int(input('enter the Kth position : '))
        st.insertafter(num)

    elif choice == 3:
        st.display1()

    elif choice == 4:
        exit(0)
    else :
        print('Wrong Choice')







