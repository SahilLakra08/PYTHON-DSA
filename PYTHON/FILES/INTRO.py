#for creating a text file :(write)-->
'''
f=open('abc.txt','w')
#this is called writing in a file.
f.write('This is a text.')
f.write('This is 2nd line.')
f.close()
'''
#w ---> will erase the existing content and create or write it with new begnining.
#for creating a new line in a text file.
'''
text='this is a text'+'\n'
f.write(text)
text='this is a second line'+'\n'
f.write(text)
f.close()
'''
#for appending or add
f=open('abc.txt','a')
text='this is a text'+'\n'
f.write(text)
text='this is a second line'+'\n'
f.write(text)
f.close()
#for read mode:rerading the file in the terminal.
f=open('abc.txt','r')
c=f.read()
print(c)
f.close()
