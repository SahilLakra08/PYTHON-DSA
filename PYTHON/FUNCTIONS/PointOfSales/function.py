def disp_menu():
    print('MacD')
    print(" Item        Price")
    print(" Burger       40")
    print(" Tea          30")
    print(" Coffee       40")
    print(" MilkShake    50")
    print("0 exit")
def place_order():
    disp_menu()
    item=input('itemName: ')
    quantity=int(input('quantity: '))
    return item,quantity
