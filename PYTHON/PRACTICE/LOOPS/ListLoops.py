#  Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
l=[1,5,20,10,30,50,120,134,323,150,490,543,500,490]
for i in l:
    if(i>500):
        break
    elif(i>150):
        continue
    elif(i%5==0):
        print(i)