
print("MacD")
print("S/no  Item        Price")
print("1     Burger       40")
print("2     Tea          30")
print("3     Coffee       40")
print("4     MilkShake    50")
moreCustomer='y'
while(moreCustomer=='y'):
    bill=0
    yn='y'
    while(yn=='y'):
        order=int(input("WHAT YOU WANT "))
        if(order==1):
            burger=int(input("how many burger"))
            bill=burger*40+bill
        elif(order==2):
            tea=int(input("how many tea: "))
            bill=tea*30+bill
        elif(order==3):
            coffee=int(input("how many coffee: "))
            bill=coffee*40+bill
        elif(order==4):
            milkshake=int(input("how many milkshake: "))
            bill=coffee*50+bill
        elif(order==0):
            yn='n'
        else:print("inappropriate choice")
        yn=input("more to order y/n: ")
    print("Bill= ",bill)
    moreCustomer=input("more customer: ")
