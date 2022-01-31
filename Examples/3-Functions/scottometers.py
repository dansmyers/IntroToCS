"""
1 Scottometer = 1 million miles
"""

def print_miles_to_scottometers(miles):
    """
    Convert the given number of miles to scottometers and print the result
    """
    
    sm = miles / 1000000
    print(sm)
    

### Main
value = float(input("Enter a number of miles: "))
print_miles_to_scottometers(value)
