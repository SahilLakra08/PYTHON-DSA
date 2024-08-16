import function
menu={'burger':40,
      'tea':30,
      'coffee':40,
      'milkshake':50}
tprice=0
yn='y'
while(yn=='y'): 
      function.disp_menu()
      titemName,tquantity=function.place_order()
      print(titemName,tquantity)
      tprice=tprice+menu[titemName]*tquantity
      yn=input('more order: ')
print(tprice)