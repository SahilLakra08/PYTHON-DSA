print("MacD")

l0=["S/no.","Item","Price"]
l1=[1,"Burger",40]
l2=[2,"Tea",30]
l3=[3,"Coffee",40]
l4=[4,"MilkShake",50]
l5=[0]

print(l0[0]     ,l0[1]     ,l0[2])
print(l1[0]     ,l1[1]     ,l1[2])
print(l2[0]     ,l2[1]     ,l2[2])
print(l3[0]     ,l3[1]     ,l3[2])
print(l4[0]     ,l4[1]     ,l4[2])
'''
print(l0)
print(l1)
print(l2)
print(l3)
print(l4)
'''
'''
print("S/no  Item        Price")
print("1     Burger       40")
print("2     Tea          30")
print("3     Coffee       40")
print("4     MilkShake    50")
'''
moreCustomer='y'
while(moreCustomer=='y'):
    bill=0
    yn='y'
    while(yn=='y'):
        order=int(input("What you want sir/mam? "))
        if(order==l1[0]):
            burger=int(input("How many burger you want? "))
            bill=burger*40+bill
        elif(order==l2[0]):
            tea=int(input("how many tea: "))
            bill=tea*30+bill
        elif(order==l3[0]):
            coffee=int(input("how many coffee: "))
            bill=coffee*40+bill
        elif(order==l4[0]):
            milkshake=int(input("how many milkshake: "))
            bill=coffee*50+bill
        elif(order==l5[0]):
            yn='n'
        else:print("inappropriate choice")
        yn=input("more to order y/n: ")
    print("Bill= ",bill)
    moreCustomer=input("more customer: ")
