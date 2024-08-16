'''
Write a program to accept percentage from the user and display the grade according to the following **
criteria:
 Marks Grade**
marks > 80: A+ grade
marks > 70 : A grade
marks > 60: B grade
marks > 50: C grade
else Failed.

'''
marks=int(input('Enter your marks un percentage % = '))
if(marks>80):
    print('A+ grade')
elif(marks>70):
    print('A grade')
elif(marks>60):
    print('B grade')
elif(marks>50):
    print('C grade')
else:
    print('Failed') 