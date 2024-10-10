# check whether a given string is pallindrome or not using recursion.
# do it without using reverse concept.


# Without Recursion :

# str1 =['M','A','L','A','Y','A','L','A','M']
# str1=input('enter the string: ')
# l=len(str1)
# i = 0
# j = l-1
# while(i<= l/2):
#     if str1[i] !=str1[j] :
#         print('Not a pallindrome')
#         exit(0)
#     else:
#         i=i+1
#         j=j-1    
# print('It is a Pallindrome')

# With Recursion :

def isPallindrome(str1,l,i,j):
    if l == 0 :
        print('String doesnt exists.')
    else:
        # base case
        if (i == j):
            return True
        elif (str1[i] != str1[j]):
                return False
    return isPallindrome(str1,l,i+1,j-1)
                
str1=input('enter the string: ')
l=len(str1)
a=isPallindrome(str1,l,0,l-1)
print(a)
# if a :
#     print('it is pallindrome')
# else:
#     print('not a pallindrome')