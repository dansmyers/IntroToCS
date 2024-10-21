"""
Randomly generated menu
"""

from random import choice, randrange

descriptions = ['non-euclidean', 'carbonized', 'impossible']
ingredients = ['aubergine', 'bonemeal', 'cuttlefish', 'durian']
preparations = ['crunchwrap', 'foam', 'confetti']

for _ in range(3):
    # Generate random indices into each list
    desc_ix = randrange(len(descriptions))
    ing_ix = randrange(len(ingredients))
    prep_ix = randrange(len(preparations))

    # Choose random selections from each list
    desc = descriptions[desc_ix]
    ing = ingredients[ing_ix]
    prep = preparations[prep_ix]

    # Output
    print(f'{desc} {ing} {prep}')

    # Remove the selected items so they can't be chosen again
    descriptions.pop(desc_ix)
    ingredients.pop(ing_ix)
    preparations.pop(prep_ix)
