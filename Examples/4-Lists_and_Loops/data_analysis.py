"""
Common data analysis operations applied to lists
"""

# Example list of recent temperatures
temps = [90, 85, 78, 77, 64, 81, 78]

### Average

# The easy way -- use the built-in sum function
average = sum(temps) / len(temps)
print(average)

# The harder way -- write our own loop
#
# Strategy: use a variable to add up all of the temp numbers ("Accumulator pattern")

total = 0  # use total to keep track of the sum of all temps

for t in temps:
    total += t   # Add t to the current total and put the result back in total
    
# After the loop completes, total stores the sum of all its elements
average = total / len(temps)
print(average)


### Minimum

# Easy way -- use the built-in min function
min_temp = min(temps)
print(min_temp)

# Harder way -- use a loop to find the smallest item
#
# Strategy: use a variable to keep track of the smallest thing we've found so far
# as we iterate through the list

min_value = temps[0]  # Initial min is the first item in the list

for t in temps:
    if t < min_value:
        min_value = t
        
print(min_value)
