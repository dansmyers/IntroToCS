# Hurricane Make-Up

## Overview

This is the make-up practice assignment for the week of 10/7. Each section below has a link to a video followed by practice problems. Work through the lab, completing each section in order. At the end, you'll submit your programs to an assignment on Canvas so that I have a record that everyone completed the make-up work.

This lab has a ***soft*** deadline of Tuesday, 10/15. I realize that we don't know how things will be after the storm, so I understand if you need a little extra time.

My plan is to still have the midterm next week, on Friday the 18th. This content **will** be part of the midterm.

## AI Usage

This is practice of fundamental content. If we were in-person, we'd do it in together in class, but we aren't. I'm asking you to do these questions **without using AI**. 

That's on the honor system, but be aware that you'll need to understand how lists and loops work for the midterm. It's to your advantage to work through these questions in a way that actually helps you learn the material.

You can always reach out to me if you have questions.

## Intro to Lists


### Video
Watch and follow along with this video: [https://www.youtube.com/watch?v=Gb4MUBxtmHI]. Remember that you can pause or rewind if you need to.

### Mixtape

`cd` into your `Lists_and_Loops` directory that you made during the video, then create a file named `mixtape.py`. Put the following starting code in your file:

```
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
```

Change the name of the mix to be whatever you want. Then use `append` to fill the `songs` list with entries. For example (sticking with the yacht rock theme):
```
songs.append('Sailing by Christopher Cross')
songs.append('Peg by Steely Dan')
songs.append('Africa by Toto')
```
Add at least five songs to your list. Print your list using
```
print(songs)
```
Run your program to verify that it prints the correct list of values in the order you appended them.

### Don't stop, make it pop
Use `pop` to remove the second and fourth items in your list, then print it the list and verify that the items were correctly removed.

Then use `insert` to put new songs at the second position and fourth position and print the list again to verify that the operation succeeded.
