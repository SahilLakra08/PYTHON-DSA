import fnc
menu={1:40,2:30,3:40,4:50}
xprice=0
yn='y'
while(yn=='y'):
    fnc.disp_menu()
    xitemNo,xquantity=fnc.place_order()
    #print(xitemNo,xquantity)
    xprice=xprice+menu[xitemNo]*xquantity
    yn=input('More Order  y/n : ')
print('Your Bill is : ',xprice)