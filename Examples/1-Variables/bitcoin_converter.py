"""
Convert Bitcoins to USD
Goal: show off input and formatted printing
"""

# Read some number of bitcoins from the terminal
user_input = input('Enter a number of bitcoins: ')

# The value returned by input is ALWAYS A STRING TYPE (str)

# The float function turns that string into a number so we can do math on it
# In this case, the converted result is saved into the variable named bitcoins
bitcoins = float(user_input)

# Convert bitcoins to dollars using the conversion factor
usd = bitcoins * 8934.61

# Print to two decimal places using a formatted string - "f-string"
# Notice the f in front of the opening quote
#
# When Python sees a name in curly braces, it treats that as a variable
# name and substitutes the value into that place in the output
#
# .2f is a format specifier that indicates printing the value to
# two decimal places
print(f'That is {usd: .2f} U.S. dollars.')
