#PROGRAM TO CHECK THE AVAILABILITY OF SPECIFIC ITEM OR NOT.
Menu={'Burger':50,'Tea':30,'Coffee':40,'MilkShake':50}
user_input=input("Enter thr item to be searched: ")
if user_input in Menu.keys():
    print(Menu[user_input])#keys is written and value is provided
else:
    print("Sorry,Doesnt exists")