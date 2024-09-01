front = 0
rear = -1
maxqueue = 10

def Enqueue(q):
    global rear

    if front == rear+1 and rear!=-1 :
        print('Queue Overflow')
    elif front ==0 and rear == maxqueue-1:
        print('Queue Overflow')
    else:
        num=int(input('Enter the number to be added: '))
        if (front !=0 and rear == maxqueue-1):
            rear=0
            q[rear]=num
        else:
            rear=rear+1
            q[rear]=num

def Dequeue(q):
    global rear
    global front

    if front==0 and rear==-1:
        print("Queue Underflow")
    elif front ==maxqueue-1:
        front=0
    elif  front == rear and rear != -1 :
            front=0
            rear=-1
    else:
            front=front+1

def display(q):
    global front
    if(rear>=front):
        for i in range(front,rear+1):
            print(q[i])
    else:
        for i in range(front,maxqueue):
            print(q[i])
        for j in range(0,rear+1):
            print(q[j])

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