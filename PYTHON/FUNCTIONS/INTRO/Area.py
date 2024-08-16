def Acircle(radius):
    return 3.14*radius*radius
def Asquare(side):
    return side*side
def Arectangle(length,breadth):
    return length*breadth


#main program
rd=int(input('Enter the Radius: '))
xArea=Acircle(rd)
print('Area of circle is ',xArea)