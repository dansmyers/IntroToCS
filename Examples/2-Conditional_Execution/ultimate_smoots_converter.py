"""
Final boss Smoots converter

This version illustrates a few alternate techniques for handling input and output
"""

# 1. Print a welcome message
print('Welcome to the Ultimate Smoots Converter v0.01')


# 2. Print the menu of choices
print('1. Feet to Smoots')
print('2. Smoots to Feet')


# 3. Ask for the user's number
user_input = input('Enter your choice: ')
choice = int(user_input)


# 4. Check for valid input
if choice < 1 or choice > 2:
    print('Invalid choice.')
    quit()  # Immediately end the program


# 5. Read the input number of units
# Key idea: I can use a variable to control whether the prompt
# asks for feet or smoots
if choice == 1:
    input_unit = 'feet'
    output_unit = 'smoots'
else:
    input_unit = 'smoots'
    output_unit = 'feet'

user_input = input('Enter a number of %s: ' % input_unit)
value = float(user_input)


# 6. Perform the appropriate conversion
FEET_PER_SMOOT = 5.5833

if choice == 1:
    output_value = value / FEET_PER_SMOOT
else:
    output_value = value * FEET_PER_SMOOT

    
# 7. Example of printing multiple variables with multiple format specifiers
# List of variables must be enclosed in ( )
print('That is %.2f %s.' % (output_value, output_unit))
