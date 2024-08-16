print('MacD')
Menu = {'Burger': 50, 'Tea': 30, 'Coffee': 40, 'MilkShake': 50}
SerialNo = 1
for k,v in Menu.items():
    print(SerialNo,'     ',k,'     ',v)
    SerialNo=SerialNo+1
moreCustomer = 'y'
while moreCustomer == 'y':
    bill = 0
    yn = 'y'
    while (yn == 'y'):
        order = int(input('What do you want sir/mam? '))
        if (order == 1):
            quantity = int(input('How many burgers do you want? '))
            bill += quantity * Menu['Burger']
        elif (order == 2):
            quantity = int(input('How many teas do you want? '))
            bill += quantity * Menu['Tea']
        elif (order == 3):
            quantity = int(input('How many coffees do you want? '))
            bill += quantity * Menu['Coffee']
        elif (order == 4):
            quantity = int(input('How many milkshakes do you want? '))
            bill += quantity * Menu['MilkShake']
        elif (order == 0):
            yn = 'n'
        else:
            print('Inappropriate choice')
        yn=input('more to order y/n: ')
    print('Bill= ',bill)
    moreCustomer=input('more customer: ')      
