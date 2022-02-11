"""
Make a mixtape - inspired by a Codecademy's taylor.swift project
"""

def tape():
    print(".------------------------.   ")
    print("|     YACHT ROCK MIX     |   ")
    print("|     __  ______  __     |   ")
    print("|    /  \\|\\.....|/  \\    |")
    print("|    \\__/|/_____|\\__/    | ")
    print("|    ________________    |   ")
    print("|___/_._o________o_._\\___|  ")

    print()
    

### Main

# Totally gratuitous ASCII art
tape()


# Create an empty list to hold the songs
songs = []


# Use the .append method to add an element to the end of the list
#
# Key idea: think of the dot as representing a message or a command
# given to the list of songs
# 
# "songs, I need you to append this new value to yourself!"
songs.append('Toto - Africa')
songs.append('Steely Dan - Peg')
songs.append('Christopher Cross - Sailing')
songs.append('Hall and Oates - I Can\'t Go For That (No Can Do)')
songs.append('Michael McDonald - What a Fool Believes')

    
# Use the remove method to remove the first item with the given value
songs.remove('Michael McDonald - What a Fool Believes')


# Use insert to put a new item at a given index
#
# Remember: the first position is index 0, the second is index 1, etc.
songs.insert(2, 'Donald Fagen - I.G.Y.')


# Use the for loop to iterate over the elements in the list
#
# This loop steps through each element of the list one at a time
#
# On the first iteration, the variable songs has the first entry in
# the list ('Toto - Africa')
#
# On the second iteration, songs has the second value in the list
# ('Steely Dan - Peg')
#
# And so forth

for song in songs:
    print(song)
