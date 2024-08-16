def disp_menu():
    print('MacD')
    print("Seriel Item        Price")
    print("1.     Burger       40")
    print("2.     Tea          30")
    print("3.     Coffee       40")
    print("4.     MilkShake    50")
    print("0 exit")
def place_order():
    disp_menu
    itemNo=int(input('Enter the itemNo: '))
    quantity=int(input("How much you want: "))
    return itemNo,quantity