# num=int(input('Enter number here: '))
#     result=10/num
#     print('result: ',result)
#try and except are for trapping the exception




#Version 1
#try:
#     num=int(input('Enter number here: '))
#     result=10/num
# except ZeroDivisionError:
#     print('Divide by Zero is not permitted')
# except ValueError:
#     print('Alphabets are not alloweded')
# except KeyboardInterrupt:
#     print('Control Characters are not allowed')
# else:
#     print('Result: ',result)




#Version 2
try:
    num=int(input('Enter number here: '))
except ValueError:
    print('Alphabets are not alloweded')
except KeyboardInterrupt:
    print('Control Characters are not allowed')
else:
    try:
        result=10/num
    except ZeroDivisionError:
        print("Divide by Zero is not permitted")
    else:
        print('Result: ',result)
    finally:
        print('10/num tested')
finally:
    print('num is tested')
    #finally means the program fails or runs,
    # finally will get exicuted either program fails or not ,
    # finally will run,chaahe error kyu na ajae program mai.