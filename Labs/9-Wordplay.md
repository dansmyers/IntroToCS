# Wordplay

<img src="https://www.artic.edu/iiif/2/e966799b-97ee-1cc6-bd2f-a94b4b8bb8f9/full/843,/0/default.jpg" width="400px" />

*Starry Night and the Astronauts*, Alma Thomas (1972), via the [Art Institute of Chicago](https://www.artic.edu/artworks/129884/starry-night-and-the-astronauts)

<br/>

This activity is adapted from Allen Downey's [*Think Python*](https://greenteapress.com/thinkpython2/html/thinkpython2010.html).

## Setup

Create a `Lab_9` directory and `cd` into it.

Go onto Canvas and download the `words.txt` file. This is a *large* list of words collected by Grady Smith as part of the Moby lexicon project, an open-source initiative to collect large free datasets for text analysis. Upload the file into your `Lab_9` directory.

Put the solution to each question below into its own file. You can choose the file names.



## Words

### Print the words

Our first program will simply print all of the words in the wordlist. Put the code below in a file named `print_words.py` and run the program.
```
"""
Print the words in the list
"""

# Open the file for reading
with open('words.txt', 'r') as f:

    # Iterate through the lines
    for line in f:

        # Strip the terminating newline character
        line = line.strip()
   
        print(line)
```
There are four interesting pieces here:

- The `open` command creates a connection to a file. `open` takes two arguments: The name of the file and a mode, which is `'r'` for reading in this example.

- Once the file is open, Python returns a **file handle** that we can use to interact with it. Here, variable `f` stores the handle to the underlying open file.

- The `with` statement wraps the file opening operation. It ensures that the file gets closed cleanly regardless of how the inner code block terminates. If an exception or return occurs, `with` will still close the file before the program terminates.

- A file is a sequence of lines, so we can iterate over them with the `for` loop. The loop in the code below steps through each line in the file one at a time. It's possible to read from files at a more granular level, like one word or one character at a time, but reading entire lines will work for this lab.

- `line = line.strip()` uses the  built-in `strip` function to remove trailing whitespace from the line. This statement removes the trailing newline character that would otherwise create an extra blank line between the words.
  


### Starts with `q`

Let's modify the basic word-printing example to print only the words that start with `q`. Put this code in a file named `starts_with_q.py`.
```
"""
Words that start with q
"""

def starts_with_q(word):
    """
    Returns True if the given word starts with q and False otherwise
    """
    return word[0] == 'q'
    

### Main
with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()
    
        if starts_with_q(line):
            print(line)
```

**Use this program as a template for all of the following programs**. Each one of your answers to the following questions should have a **function** that implements whatever tests are required to answer the problem.


### Starts with `q` but not `qu`

<img src="https://en.numista.com/catalogue/photos/albanie/5eb334f6befca9.58828003-360.jpg" width="100px" />

*A qindar is a subunit of the lek, Albania's unit of currency*.

<br/>

Print the words that start with `q` but not `qu`.

Tip: You might be tempted to try something like the following in your function.
```
return word[0] == 'qu'
```
**This won't work** because `word[0]` is a single character, so it can never be equal to two characters. Therefore, the statement will always return `False`. Think about how to test the first and second characters and combine the two tests with `and`.

### Long words

Recall that you can use `len` to get the number of characters in a string, like so

```
num_chars = len(word)
```

Print all of the words with 18 or more characters.

### Ends with `x`

Recall that there are two ways to access the last character of a word:

```
word[len(word) - 1]

word[-1]
```

Print all of the words that end with `x`

### I'm thinking of a word

I'm thinking of a word that starts with `he` and ends with `he`. What could it be?

### Slicing

**Slicing** is a way to pull out a piece of a string (or list) as a substring (or sublist). To take a slice, use a colon in square brackets and specify the range of index positions you want to slice out.
```
# Slice out the characters from index 1, up to BUT NOT INCLUDING index 5
subword = word[1:5]
```
Slicing works similar to `range`: it starts at the beginning index and goes up to, *but doesn't include* the stopping index. In the example above, if the word is `acidic`, the subword would be `cidi`, formed from the characters at positions 1 to 4.

If you slice from the beginning of the string, you don't have to specify 0 as the starting index:
```
# Slice the first two characters
first_two_letters = word[:2]
```
Similarly, you can automatically slice to the end of the string if you don't specify the ending index:
```
last_two_letters = word[len(word) - 2:]
```

Repeat the previous problem, but use slicing to isolate substrings from the beginning and end of the word, then test if both substrings are equal to `'he'`

### No vowels

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Crwth_rem.jpg/800px-Crwth_rem.jpg width="200px" />

*The Welsh crwth*

<img src=https://upload.wikimedia.org/wikipedia/commons/9/9f/Western_Cwm_and_Lhotse.jpg width="300px" />

*The Western Cwm (a glaciated valley) on Mt. Everest with the Lhotse Face in the background*

<br/>

Find all of the words that contain no vowels and no `y`.

Tip: An easy way to test if a letter is vowel or y is
```
# Test if letter is a vowel or y
if letter in 'aeiouy':
    return False
```
Loop over the characters in the word and test each one to see if it's a vowel. If you find a vowel or a `y`, the test method can immediately `return False`. If you make it all the way through the loop and never find a vowel or `y`, `return True`.


### Abecedarian words

Let's say that a word is *abecedarian* if its letters are in alphabetical order, allowing for repeated letters. For example, *effort*, *ghosty*, and *beefily* are abecedarian words. Print all the abecedarian words in the list.

Remember that you can compare characters using the standard relational operators `<` and `>`. All of the words in the list are lowercase, so you don't have to worry about any upper vs. lower case comparison issues.


### TACOCAT is TACOCAT backwards

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cf45aa02-f54d-4cab-a8e8-4e43c0ed6c74/dcn8689-dc15f569-0e2e-4552-b107-12fc38995653.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NmNDVhYTAyLWY1NGQtNGNhYi1hOGU4LTRlNDNjMGVkNmM3NFwvZGNuODY4OS1kYzE1ZjU2OS0wZTJlLTQ1NTItYjEwNy0xMmZjMzg5OTU2NTMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.UopOXSHXupOZqB0oUtH4dPwiENGDw3zC1nxStTpzhCM" width="30%" />

<br/>

Find all the palindromes in the word list. Use a function called `is_palindrome` that takes `word` as input and returns `True` if it is a palindrome. Don't use any function that reverses the word.

Tip: Use a loop that compares pairs of letters, starting at the outermost letters (indexes 0 and `len(word) - 1`) and working inwards. If you find a pair that doesn't match, return `False` immediately. If you succeed in checking all pairs, return `True`.

```
# Calculate the index of the middle letter using integer division
middle = len(word) // 2

for i in range(middle):
    # Check if the letter at position i and its opposite letter are the same
    
    # If not, return False immediately

```
The tricky part: How can you determine the index of the letter that is opposite letter `i`? Think about subtracting from `len(word)` or by using negative indexing.

### Triple double letters

The word `balloon` has two consecutive pairs of double letters. I'm thinking of a word that has *three* **consecutive** pairs of double letters. What could it be?


# Drawing with Pillow

<img src="https://www.cooperhewitt.org/wp-content/uploads/2013/06/46575_b57abb49b0eea16e_b.jpg" width="300px" />

Anni Albers, *Éclat* (1975), via [Cooper Hewitt](https://www.cooperhewitt.org/2013/06/12/a-puzzling-order/) 


### Starter code

Start by putting the following program into a file named `basic_drawing.py` and then running it. It will produce a file named `rect.png` that you can click on to open and examine.

```
"""
Rectangle drawing with Pillow
"""

from PIL import Image, ImageDraw

# Create a blank canvas with white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw a red rectangle
#
# The first argument is a list of point pairs defining the upper-left and lower-right corners
# of the rectangle
#
# fill is the color
draw.rectangle([(50, 50), (300, 200)], fill='red', outline='black', width=2)

# Save the image
image.save('rect.png')
```


### Image geometry

Drawing is done in units of **pixels**.

Think of the image as a 2-D plane. Every pixel can be represented by an (x, y) coordinate on the plane, like you would expect.

There is one detail, however, that's different from normal coordinate geometry. The origin, (0, 0), is the ***upper-left*** pixel. Increasing the x value corresponds to moving right on the image, as normal, but increasing y corrresponds to moving **down**.

```
(0, 0)   ------------------------> x
    +------------------------------------------+
    |                                          | 
|   |                                          |
|   |                                          | 
|   |                                          |
|   |                                          |
v   |                                          |
y   |                                          |
    |                                          |
    +------------------------------------------+
```

For example, the pixel (50, 100) is at the point that is 50 pixels to the right and 100 pixels down. That might look something like this, with the pixel twice as far down the image as it is to the right.
```
(0, 0)   ------------------------> x
    +------------------------------------------+
    |                                          | 
|   |                                          |
|   |                                          | 
|   |                                          |
|   |       + (50, 100)                        |
v   |                                          |
y   |                                          |
    |                                          |
    +------------------------------------------+
```

### Drawing rectangles

Look at the example drawing command:
```
draw.rectangle([(50, 50), (300, 200)], fill='red', outline='black', width=2)
```
First, notice that this call uses dot notation. The `draw` object supports a number of methods that can be used to implement drawing behaviors. We're telling that `draw` object to create a rectangle with the given properties.

The function has four arguments:

- A **list** of point pairs that define the upper-left and lower-right corners of the rectangle. Here, the upper-left point is (50, 50) and the lower-right point is (300, 200)

- `fill`, which is fill color. This can be a string, like `'red'` or `'blue'`, or a specific red-green-blue color. More on that later.

- `outline` is the border color and `width` is the thickness of the border.

This introduces a new feature: **named input parameters**. This style of function calling allows you to specify inputs by name. If you don't want to specify a particular input, you can leave it out and the function will use a default value. For example, to make a blue rectangle with no border:
```
# Draw a rectangle with the outline and width parameters omitted
draw.rectangle([(50, 50), (300, 200)], fill='blue')
```

### Jam

Modify the example program to add more rectangles to the image. Experiment with changing the positions, sizes, colors, and outlines.


## Homage to *Homage to the Square*

<img src="https://www.guggenheim.org/wp-content/uploads/1959/01/61.1590_ph_web-1.jpg" width="400px" />

Josef Albers, *Homage to the Square: Apparition* (1959), via the [Guggenheim](https://www.guggenheim.org/artwork/173)

### Josef Albers

Josef Albers was a German-American painter, art educator, and theorist, known for his contributions to abstract painting and his writings on color interaction. Born in 1888 in Westphalia, Germany, into a family of craftsmen, he first learned trade skills, then trained as a painter and stained-glass maker. He enrolled in the Bauhaus as a student in 1920, then joined the faculty as a stained-glass maker in 1922. Albers married his wife Anni, a weaver, in 1925. She would become one of the twentieth century’s leading textile artists.

The Bauhaus ("building house") was a major art and design school founded by the architect Walter Gropius in 1919. It was famous for combining the fine arts with new materials and methods of industrial production. The philosophy and alumni of the school had a major influence on 20th Century design.

The Albers fled Germany in 1933 after the Bauhaus closed under Nazi pressure and Josef accepted a new position at Black Mountain College in North Carolina, an experimental liberal arts school that emphasized hands-on learning and art making. Black Mountain had been founded by John Andrew Rice, an eccentric Rollins professor who was fired in the early 1930s by Hamilton Holt, along with nine other faculty who refused to sign a loyalty pledge. Before closing in 1957, the college would go on to host a number of figures from the mid-century avant-garde, including the composer John Cage and architect Buckminster Fuller, who constructed the first geodesic domes at Black Mountain. Albers moved to Yale in 1949.

Albers began the *Homage to the Square* series in 1949, accumulating more than 1,000 entries before his death in 1976. The pieces use a formal composition of three or four nested squares and were created to investigate the properties of colors and their interactions.

Let’s write a graphical program that will create our own nested square images inspired by *Homage*.

### Strategy

Our basic method is as follows:

- Initialize a square canvas

- Initialize the starting upper-left corner as (0, 0) and the starting square size

- Use a loop to generate the nested square, where the number of iterations controls the number of squares

- Each iteration chooses a random color, then draws a square at the current coordinates at the current size

- Then adjust the coordinates and size to move to the position of the next square

### Starter code

```
"""
Homage to Homage to the Square
"""

from PIL import Image, ImageDraw

NUM_SQUARES = 3

# The upper-left corner of the current square
ul = (0, 0)

# The size of the initial largest square in pixels
size = 400

# Create the square canvas
image = Image.new("RGB", (size, size), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Loop to draw nested square
for i in range(NUM_SQUARES):

    # Calculate the lower-right corner of the current rectangle
    lr = (ul[0] + size, ul[1] + size)

    # Draw at the current position and size
    draw.rectangle([ul, lr], fill="red", outline="black", width=2)

    # Move inwards to the next position
    #
    # These updates will give you a shift similar to Albers' composition
    next_x = ul[0] + size / 8;
    next_y = ul[1] + size / 6;
    ul = (next_x, next_y)

    # Reduce the side length
    size = 3 * size / 4;

image.save('homage.png')
```

### Run

Copy the code into your Codespace and run it. You should produce `homage.png` with nested squares. This version is only colored red with black lines between the squares.

### Random colors

Now modify the program to choose a random color at the beginning of each loop iteration. Put this inside the `for` loop before you call `draw.rectangle`.
```
# Generate a random RGB color
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255) 
color = (r, g, b)
```
Update the `draw` method to be:
```
draw.rectangle([ul, lr], fill=color, outline="black", width=2)
```
The `fill` parameter has been changed to use the random color.

### Jam

Once you have the basic version working, play around with the number of squares and the positioning. Experiment with changing the part of the loop that moves and resizes the square for the next iteration and observe how those changes affect the result.
