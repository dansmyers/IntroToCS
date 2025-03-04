# Homage

<img src="https://www.guggenheim.org/wp-content/uploads/1959/01/61.1590_ph_web-1.jpg" width="400px" />

Josef Albers, *Homage to the Square: Apparition* (1959), via the [Guggenheim](https://www.guggenheim.org/artwork/173)

## Overview

This lab will allow you to practice writing loops and using lists. We'll also introduce some more graphical operations using the Pillow library, which you may recall from Project 1.

As you're working, think carefully about the behavior of your loops. Remember that the `for` loop is tricky because the execution is more complex than its visual appearance. Always think about the sequence that you're iterating over and the exact sequence of values that it contains. Remember that the default behavior of the loop is to step through the items of the sequence, one at a time and in their given order.


## Setup

Create a `Lab_7` directory in your workspace and `cd` into it.
```
mkdir Lab_7
```
```
cd Lab_7
```
The questions will tell you how to create and name your Python scripts.


## Drawing with Pillow

<img src="https://www.cooperhewitt.org/wp-content/uploads/2013/06/46575_b57abb49b0eea16e_b.jpg" width="300px" />

Anni Albers, *Éclat* (1975), via [Cooper Hewitt](https://www.cooperhewitt.org/2013/06/12/a-puzzling-order/) 


### Starter code

Start by putting the following program into a file named `basic_drawing.py` and then running it. It will produce a file named `drawing.png` that you can click on to open and examine.

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
First, notice that this call uses dot notation. The `draw` object supports a number of methods that can be used to implemented drawing behaviors. We're telling that `draw` object to create a rectangle with the given properties.

There function has four arguments:

- A list of point pairs that define the upper-left and lower-right corners of the rectangle. Here, the upper-left point is (50, 50) and the lower-right point is (300, 200)

- `fill`, which is fill color. This can be a string, like `'red'` or `'blue'`, or a specific red-green-blue color. More on that later.

- `outline` is the border color and `width` is the thickness of the border.

This introduces a new feature: **named input parameters**. This style of function calling allows you to specify inputs by name. If you don't want to specify a particular input, you can leave it out and the function will use a default value. For example, to make a blue rectangle with no border:
```
# Draw a rectangle with the outline and width parameters omitted
draw.rectangle([(50, 50), (300, 200)], fill='red')
```

### Jam

Modify the example program to add more rectangles to the image. Experiment with changing the positions, sizes, colors, and outlines.


## Homage to *Homage to the Square*

<img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Grafik_nach_Josef_Albers.jpg" width="400px" />

*via [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/a/ab/Grafik_nach_Josef_Albers.jpg)*

### Josef Albers

Josef Albers was a German-American painter, art educator, and theorist, known for his contributions to abstract painting and his writings on color interaction. Born in 1888 in Westphalia, Germany, into a family of craftsmen, he first learned trade skills, then trained as a painter and stained-glass maker. He enrolled in the Bauhaus as a student in 1920, then joined the faculty as a stained-glass maker in 1922. Albers married his wife Anni, a weaver, in 1925. She would become one of the twentieth century’s leading textile artists.

(The Bauhaus, "building house", was a major art and design school founded by the architect Walter Gropius in the early-20th Century. It was famous for integrating art and new materials and methods of industrial production. The philosophy and alumni of the school had a major influence on Twentieth Century design.)

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
