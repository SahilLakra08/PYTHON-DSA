#how to write multiple lines
f=open('myprg.txt','a')
yn='y'
while yn=='y':
    text=input("Enter text here= ")
    text1=text+'\n'
    f.write(text1)
    yn=input('more_y ')
f.close()
#display or read
f=open('myprg.txt','r')
c=f.read()
print(c)
f.close()