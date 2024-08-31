
def BubbleSort(A,l):
    for i in range(1,l,1):
        for j in range(0,l-i,1):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]


def RowSum(marks):
    total=[0 for i in range(5)]
    Merit=[0 for i in range(5)]
    for i in range(5):
        for j in range(5):
            total[i]=total[i]+marks[i][j]
    for i in range(5):
        # print('Total marks of student',i+1,'is',total[i])
        Merit[i]=total[i]/5
        # print('Merit of student',i+1,'is',Merit,'%')
    BubbleSort(Merit,5)
    print(Merit)
    for i in range(5):
        print('Merit of student',i+1,'is',Merit[i],'%')



marks=[[70,75,80,90,95],[33,44,55,66,77],[34,54,23,56,43],[45,89,67,56,68],[67,54,45,89,56]]
RowSum(marks)

