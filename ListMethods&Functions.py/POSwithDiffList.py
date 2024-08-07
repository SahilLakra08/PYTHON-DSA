
#MAIN TWO LISTS OF MENU AND PRICE SEPERATELY:H/W
print("MacD")
price=[]
Menu=[]
yn='y'
while(yn=='y'):
    item=input("Enter ItemName= ")
    price1=int(input("Enter the Price= "))
    Menu.append(item)
    price.append(price1)
    yn=input("More:y")
print(Menu)
print(price)