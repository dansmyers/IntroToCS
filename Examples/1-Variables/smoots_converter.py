"""
Convert a length in feet into smoots
CMS 120
"""

# Declare constant
FEET_PER_SMOOT = 5.5833

# Read length in feet and convert it to a float type
user_input = input('Enter a length in feet: ')
length_in_feet = float(user_input)

# Convert
length_in_smoots = length_in_feet / FEET_PER_SMOOT

# Print to two decimal places
print(f'Length in Smoots: {length_in_smoots: .2f}')
