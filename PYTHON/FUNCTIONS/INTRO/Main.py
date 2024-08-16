#Main Program
import Liberary
Liberary.abc()
Liberary.abc()
x=int(input('FirstNo: '))
y=int(input('SecondNo: '))
result=Liberary.add2(x,y)
print('Addition= ',result)
mylst=Liberary.createList()
print(mylst)
xname,xrollNo,xage=Liberary.myform()
print(xname,xrollNo,xage)

rd=int(input('Enter the Radius: '))
xArea=Liberary.Acircle(rd)
print('Area of circle is ',xArea)