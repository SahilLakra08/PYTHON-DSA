def diagonalSum(lst):
    sum1=0
    sum2=0
    for i in range(0,4):
        for j in range(0,4):
            lst[i][j]=i+j
            if(i==j):
                sum1=sum1+lst[i][j]
            elif(i+j==3):
                sum2=sum2+lst[i][j]
            print(i+j,end=' ')
        print('')
    print('sum1:',sum1)
    print('sum2:',sum2)



lst=[[0 for j in range(4)]for i in range(4)]
diagonalSum(lst)
#Homework: do with taking no. of rows=m, no. of columns=n,then do it again!!!!