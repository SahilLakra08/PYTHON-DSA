tple=(1,2,3,'India',22.7,'a+3x')
print(tple)
print(tple[0])

#tuples contains contants means it has elements which remains unchanged .like company name etc
#we cannot can elements forcefully like we do in list
#tple[4]=91.2
#print(tple)
#while and for loop are same

#for changing elements first convert tuple into the list and make changes and
#then again change list into tupe
list_tple=list(tple)
print(list_tple)
list_tple[4]=91.2
print(list_tple)
tpl_list=tuple(list_tple)
print(tpl_list)


#for only one element in a tuple ,(comma)is important eg:
tp1=('a',)
#comma declares that this is tuple with one element