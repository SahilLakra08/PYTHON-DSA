# # queue can be used by array and linked list.
# # it follows FIFO(first in first out)
# program to implement circular queue


# LINEAR QUEUE:
front = 0
rear = -1
maxqueue = 10

def Enqueue(q):
    global rear
    if rear == maxqueue-1:
        print('Queue Overflow')
    else:
        num=int(input('Enter the number to be added: '))
        rear=rear+1
        q[rear]=num

def Dequeue(q):
    global rear
    global front
    if rear == -1 and front == 0 :
        print('Queue Empty or Underflow')
    else:
       
        if front == rear :
            front=0
            rear=-1
        else:
            front=front+1

def display(q):
    global front
    for i in range(front,rear+1):
        print(q[i])

q=[0 for i in range (maxqueue)]
while(True):
    print('      QUEUE OPERATION      ')
    print('         1.ENQUEUE(ADD)      ')
    print('         2.DEQUEUE(DELETE)       ')
    print('         3.DISPLAY       ')
    print('         4.EXIT       ')
    choice=int(input('Enter your choice: '))

    if choice == 1:
        Enqueue(q)
    elif choice == 2:
        Dequeue(q)
    elif choice == 3:
        display(q)
    elif choice == 4:
        exit(0)
    else :
        print('Wrong Choice')