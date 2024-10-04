# Structured Testing

## Overview

**Unit testing** is a an approach to program testing that involves testing each functions as a basic independent unit. If you can verify the correctness of the lowest-level functions in your program, then you can test and verify the correctness of the next highest level, and so forth, until you have a complete test suite that gives you confidence that your entire program works correctly.

**Testing is challenging** because programs can be wrong in subtle ways and it's hard to to anticipate all of the possible bugs that might exist when you're writing tests. After all, if you could easily anticipate a particular bug, it would be easier to avoid writing it in the first place.

**Structured testing** (also known as *basis testing*, and a bunch of other name variations) is an approach to designing function-level tests such that all paths through the function are tested.


## Example: Loyalty Program

Let's imagine a customer-loyalty program that gives percentage discounts on purchases based on the customer's years of loyalty and a membership tier:

- Customers get a 1% discount for each year of loyalty. New customers with less than 1 full year get a .5% discount and the maximum discount is 5%.
- Customers also get a 1% discount for each full $100 of the purchase amount. For example, a $250 purchase gets an extra 2% discount.
- There are two tiers: Elite and Standard. Elite tier customers get an extra 2.5% discount.
- The maximum discount under any combination of inputs is capped at 20%.

Here's an implementation of this system. Make a file named `discount.py` in your `Functions` directory and copy the code. Team up with your neighbor and experiment with writing some test cases.

We'll then talk about some issues with this code and how to test it in a structured way.

```
"""
Calculate a customer loyalty discount -- illustrate structured basis testing
"""

def calculate_discount_percent(amount, years, tier):
    """
    Calculate a customer's discount

    Inputs
    amount: the base purchase price
    years: number of years customer has been a loyalty member
    tier: 'Standard' or 'Elite' 

    Returns
    the percentage discount applied to this amount for this customer
    """

    # Customers get 1% discount for each year of loyalty, min of .5, max of 5
    if years == 0:
        discount = .5
    elif years > 5:
        discount = 5
    else:
        discount = years

    # Elite tier customers get an additional 2.5% discount
    if tier == 'Elite':
        discount += 2.5

    # Customers also get 1% discount for each $100 purchase
    #
    # Tip: Use // for integer division
    points = amount // 100
    discount += points

    # The maximum discount is 20%
    discount = min(discount, 20)

    return discount


def calculate_discounted_price(amount, years, tier):
    """
    Calculate a customer's discount

    Inputs
    amount: the base purchase price
    years: number of years customer has been a loyalty member
    tier: 'Standard' or 'Elite' 

    Returns
    the final price after applying the loyalty discount
    """
    percent_discount = calculate_discount_percent(amount, years, tier)
    return amount * percent_discount / 100


### Main
print(calculate_discount_percent(99, 10, 'Elite'))

```
