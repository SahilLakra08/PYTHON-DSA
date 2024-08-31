# # stack can be declared with help of array and linked list.
# # have LIFO.
#   homework:
# convert number to binary,octal,hexadecimal:




# stack operations:
# 1.push2.pop
# 3.display
# 4.exit
# 5.enter your choice

top = -1
maxStack=10

def push1(s):
    global top
    if (top==maxStack-1):
        print('Stack Overflow')
    else:
        num=int(input('Enter the element to be pushed in stack: '))
        top=top+1
        s[top]=num
        print(top)

def pop1(s):
    global top
    if(top==-1):
        print('Stack Empty')
    else:
        top=top-1
def display(s):
    global top
    for i in range(top+1,0):
        print(s[i])


s=[0 for i in range(maxStack)]
print(s)
while(True):
    print('     STACK OPERATION      ')
    print('         1.PUSH      ')
    print('         2.POP       ')
    print('         3.DISPLAY       ')
    print('         4.EXIT       ')
    choice=int(input('Enter your choice: '))

    if choice == 1:
        push1(s)
    elif choice == 2:
        pop1(s)
    elif choice == 3:
        display(s)
    elif choice == 4:
        exit(0)
    else :
        print('Wrong Choice')
