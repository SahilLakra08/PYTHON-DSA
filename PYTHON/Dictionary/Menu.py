#PROGRAM TO CREATE ALL THE MENU ITEMS IN THE DICTIONARY.

menu={}
yn='y'
while(yn=='y'):
    k1=input("Item_Name: ")
    v1=int(input("Item_Price: "))
    menu[k1]=v1
    yn=input("More Item to add in the Menu=y")
print(menu)

print(menu['burger'])