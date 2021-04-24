import sys
raw_input = input
# My Menu
print('--')
print('Welcome to the String Reversal Program')
print('--')
print('1. Slicing')
print('2. For Loop')
print('3. While Loop')
print('4. List')
print('5. Recursion')
print('6. Reversed()')
print('7. Close the program')
print('--')

# User Selection
menu_selection = int(input('Enter your selection: '))

# Menu Validation
while menu_selection < 1 or menu_selection > 7:
    print('Invalid Selection, try again!')
    menu_selection = int(input('Enter 1, 2, 3, 4, 5, 6, or 7: '))

# Perform the users selection 1 Through 7

# Slicing
if menu_selection == 1:
    userInput1 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing... intense things are happening!')
    print('\n')
    reverseString1 = userInput1[::-1]
    print('Reversed using Slicing', reverseString1)

# For Loop
elif menu_selection == 2:
    userInput2 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing... intense things are happening!')
    print('\n')
    temp = ""
    for char in userInput2:
        temp = char + temp
    print('Reversed using For Loop', temp)

# While Loop
elif menu_selection == 3:
    userInput3 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing.. intense things are happening!')
    print('\n')
    temp = ""
    length = len(userInput3) -1
    while length >=0:
        temp = temp + userInput3[length]
        length = length -1
    print('Reversed using While Loop', temp)

# List
elif menu_selection == 4:
    userInput4 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing.. intense things are happening!')
    print('\n')
    temp_list = list(userInput4)
    temp_list.reverse()
    print('Reversing using a List...')
    print('\n')
    print(''.join(temp_list))


# Recursion
elif menu_selection == 5:
    userInput5 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing.. intense things are happening!')
    print('\n')
    def reverse_rec(userInput5):
        if len(userInput5) == 0:
            return userInput5
        else:
            return reverse_rec(userInput5[1:]) + userInput5[0]
    print('Reversing using Recursion...')
    print('\n')

    print(reverse_rec(userInput5))

# Reversed()
elif menu_selection == 6:
    userInput6 = raw_input('Enter your string!: ')
    print('\n')
    print('Processing.. intense things are happening!')
    print('\n')
    reverseString6 = userInput6
    reverse_str = ''.join(reversed(userInput6))
    print('Reversing using Reversed()', reverse_str)

# End Program
elif menu_selection == 7:
    sys.exit
    print('Goodbye!')



