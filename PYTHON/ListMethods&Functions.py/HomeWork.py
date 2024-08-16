print('MacD')
l1=['serielNo',1,2,3,4]
l2=['item','burger','tea','coffee','milkshake']
l3=['price',40,30,40,50]
l4=[0]
print(l1[0],     l2[0],     l3[0])
print(l1[1],     l2[1],     l3[1])
print(l1[2],     l2[2],     l3[2])
print(l1[3],     l2[3],     l3[3])
print(l1[4],     l2[4],     l3[4])
moreCustomer='y'
while(moreCustomer=='y'):
    bill=0
    yn='y'
    while(yn=='y'):
        order=int(input('What you want sir/mam? '))
        if(order==l1[1]):
            burger=int(input('How many burger you want? '))
            bill=burger*l3[1]+bill
        elif(order==l1[2]):
            tea=int(input('How many tea: '))
            bill=tea*l3[2]+bill
        elif(order==l1[3]):
            coffee=int(input('How many coffee: '))
            bill=coffee*l3[3]+bill
        elif(order==l1[4]):
            milkshake=int(input('How many milkshake: '))
            bill=milkshake*l3[4]+bill
        elif(order==l4[0]):
            yn='n'
        else:print('inappropriate choice')
        yn=input('more to order y/n: ')
    print('Bill= ',bill)
    moreCustomer=input('more customer: ')