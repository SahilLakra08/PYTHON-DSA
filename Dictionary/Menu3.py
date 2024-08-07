Menu={'Burger':50,'Tea':30,'Coffee':40,'MilkShake':50}
serielNo=1
for k,v in Menu.items():
    print(serielNo,'     ',k,'     ',v)
    serielNo=serielNo+1

#PRINT ITEMS
for k in Menu.keys():
    print(k)
#PRINT VALUES
for v in Menu.values():
    print(v)

#IF THE PRICE OF ITEMS IS INCREASED
Menu['Burger']=90
print(Menu)
#FOR ADDING NEW ITEM IN MENU
Menu['Dal Makhani']=100
print(Menu)