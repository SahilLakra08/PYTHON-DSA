f=open('myxyz.txt','a')
text=input("Enter text here= ")
text='y'
while (text!='BYE'):
    text=input('')
    text1=text+'\n'
    if (text!='BYE'):
        f.write(text1)
f.close()
    
#display or read
f=open('myxyz.txt','r')
c=f.read()
print(c)
f.close()

