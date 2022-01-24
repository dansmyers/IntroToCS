"""
Test if an input number is even or odd

Illustrates the use of the modulus operator to test for divisibility
"""

user_input = input('Type a number.')
value = int(user_input)

if value % 2 == 0:
    print('Even.')
else:
    print('Odd.')
    
print('Done.')
