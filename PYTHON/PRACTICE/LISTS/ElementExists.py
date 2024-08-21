#Check if element exists in list in Python
L = [10, 20, 30, 40, 50, 60, 70, 80]
num = int(input('Enter the number you want to check: '))

# Flag to check if number exists
exists = False

# Loop through the list to check if number exists
for i in range(len(L)):
    if num == L[i]:
        exists = True
        break

# Print the result based on the flag
if exists:
    print('exists')
else:
    print('Does not exist')
