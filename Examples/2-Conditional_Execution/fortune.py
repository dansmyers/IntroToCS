"""
Print a randomly chosen message each time the program is run.
"""

# Import the random function from the random module
from random import random

# Generate a random value in [0, 1)
r = random()

# Use r to choose one of the output options
if r < .20:
    print("The course of true love never did run smooth. - A Midsummer Night's Dream: I, i")

elif r < .40:
    print("We know what we are, but know not what we may be. - Hamlet: IV, v")
    
elif r < .60:
    print("If music be the food of love, play on. - Twelfth Night: I, i")

elif r < .80:
     print("Brevity is the soul of wit. - Hamlet: II, ii")

else:
    print("We are such stuff as dreams are made on, and our little life is rounded with a sleep. - The Tempest: IV, i")
    
