"""
Checking user input
"""

INCHES_PER_FOOT = 12

# Read length in feet
feet = float(input('Enter a length in feet: '))

# Verify the input is non-negative
#
# If it's negative, print an error and quit immediately
if feet < 0:
  print('Length must be non-negative.')
  quit()

# Convert to units of inches
inches = feet * INCHES_PER_FOOT

# Print with formatted string
print(f'{feet} ft. is {inches: .2f} in.')
