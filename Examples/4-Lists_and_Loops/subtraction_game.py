"""
Subtraction game

Start with a pile of 21 stones
Players take turns removing 1, 2 or 3 stones from the pile
The player who takes the last stone WINS in this version

A variation makes the final stone-taker the loser

Illustrates using a loop and try-except to force valid input
"""

stones = 21
current_player = 1

looping = True
while looping:
    print()
    print(f'It is player {current_player}\'s turn. There are {stones} stones.')

    # Use a while loop to force the user to give valid input
    getting_input = True
    while getting_input:

        # Run the code inside the try block - if an exception occurs then Python jumps
        # to the except block to handle it
        #
        # Here, if the user types invalid input that causes a ValueError, the except
        # block will remind them to enter 1, 2, or 3
        #
        # The loop repeats until the user enters a valid input option
        try:
            remove = int(input('Take 1, 2, or 3 stones: '))

            if remove < 1 or remove > 3 or remove > stones:
                print('That is not a valid choice.')
            else:
                getting_input = False
        except ValueError:
            print('Enter 1, 2 or 3.')

    # Reduce the number of stones
    stones -= remove
    print(f'There are now {stones} stones remaining.')

    # The player who takes the last stone WINS in this version
    if stones == 0:
        print(f'Player {current_player} wins!')
        looping = False
    else:
        # Switch to the other player
        current_player = (current_player % 2) + 1
