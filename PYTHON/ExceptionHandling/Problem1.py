# f=open('India.txt','r')
# c=f.read()
# print(c)

try:
    f=open('India.txt','r')
except FileNotFoundError:
    print('Your file is not found')
    A=input("Want to create a new file Yes or NO: ")
    if(A=='Yes'):
        f=open('India.txt','w')
        text=input("Write Here: ")
        f.write(text)
        f.close()
else:
    c=f.read()
    print(c)
    f.close()    