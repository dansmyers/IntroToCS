"""
Binet's Formula
"""

# Imports go right after the docstring
from math import sqrt

# Read the value of n from the terminal
user_input = input('Enter the value of n: ')
n = int(user_input)

# Calculate, breaking the big calculation up into variables
phi = (1 + sqrt(5)) / 2
phi_to_the_n = phi ** n

phi_sub = (1 - sqrt(5)) / 2
phi_sub_to_the_n = phi_sub ** n

diff = phi_to_the_n - phi_sub_to_the_n

f_n = (1 / sqrt(5)) * diff

# Print
print(f_n)
