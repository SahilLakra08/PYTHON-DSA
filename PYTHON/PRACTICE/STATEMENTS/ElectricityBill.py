# Write a program to calculate the electricity bill
# (accept the number of unit from user)according to following criteria:  
#          Unit                      Price
#      first 100 units              no charge
#      next 100 units               Rs 5 per Unit 
#      After 200 units              Rs 10 per unit
# (For example if input units is 350 than total bill amount is Rs2000)
unit=int(input('Enter the number of units: '))
bill_amount=0
if(unit<=100):
    print('Your total bill amount is:Rs 0')
elif(100<unit<=200):
    bill_amount=(unit-100)*5
    print('Your total Bill Amount is: Rs',bill_amount)
elif(unit>200):
    bill_amount=(500+(unit-200)*10)
    print('Your total bill amount is: Rs',bill_amount)