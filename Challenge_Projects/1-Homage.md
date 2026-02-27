# Challenge Project: Homage

<img src="https://www.guggenheim.org/wp-content/uploads/1959/01/61.1590_ph_web-1.jpg" width="400px" />

Josef Albers, *Homage to the Square: Apparition* (1959), via the [Guggenheim](https://www.guggenheim.org/artwork/173)

## Due 3/13 (the day before Spring Break, after the midterm)

## Overview

This project will allow you to practice drawing and graphics in Python. There are three parts:

1. Basic drawing, demonstrating how to use coordinates, shapes, and colors
2. Implementing a program that generates randomized art in the style of Josef Albers' *Homage to the Square*, as seen above
3. Making your own generative art program

Remember that this project is **optional**, but completing it will raise your final course grade by one part of a letter (e.g., B to B+).

## Setup

Create a `Challenge-1-Homage` directory:
```
mkdir Challenge-1-Homage
```
Then `cd` into it:
```
cd Challenge-1-Homage
```

## Drawing with Pillow

<img src="https://www.cooperhewitt.org/wp-content/uploads/2013/06/46575_b57abb49b0eea16e_b.jpg" width="300px" />

Anni Albers, *Éclat* (1975), via [Cooper Hewitt](https://www.cooperhewitt.org/2013/06/12/a-puzzling-order/) 


### Starter code

This first section will allow you to practice basic drawing using Pillow, the same image library we used in Project 1. Work through the steps below and experiment with the different features.

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

You can only draw in units of whole-numbered pixels. Fractional placements aren't allowed.

### Drawing rectangles

Look at the example drawing command:
```
draw.rectangle([(50, 50), (300, 200)], fill='red', outline='black', width=2)
```
First, notice that this call uses dot notation. The `draw` object supports a number of methods that can be used to implement drawing behaviors. We're telling that `draw` object to create a rectangle with the given properties.

The function has four arguments:

- A **list** of point pairs that define the upper-left and lower-right corners of the rectangle. Here, the upper-left point is (50, 50) and the lower-right point is (300, 200). The placement of the commas is a bit tricky: there is a comma between the coordinates of each point and one in between the points to order them in the list.

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

<img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Grafik_nach_Josef_Albers.jpg" width="300px" />

*via [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/a/ab/Grafik_nach_Josef_Albers.jpg)*

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

## Masterpiece

<img src="https://www.maxkohler.com/assets/notes/schlitzgobelin_gunta_stoelzl.jpg_1728511801.jpg" width="300px" />

Gunta Stölz, *Slit Tapestry Red-Green* (1927-28). Via [Bauhaus Archive](https://open-archive.bauhaus.de/eMP/eMuseumPlus?service=direct/1/ResultDetailView/result.inline.list.t1.collection_list.$TspTitleImageLink.link&sp=13&sp=Sartist&sp=SfilterDefinition&sp=0&sp=1&sp=1&sp=SdetailView&sp=131&sp=Sdetail&sp=0&sp=T&sp=0&sp=SdetailList&sp=0&sp=F&sp=Scollection&sp=l60412).

Now use these techniques to create *your own generative art program*. Your program shoud have some strategy that it implements to create an artistic composition that incorporates randomness in at least one of its elements.

You have broad freedom to create what you want, with a few guidelines:

- There must be some strategy or planned approach used to structure the output.

- You have to create something with enough complexity to be interesting. You can't just put a few random rectangles on the screen.

- You must incorporate some randomness to determine the output, so that you get a different output every time you run the program. This can include random colors but needs to be more than that.

- You're free to use an AI to help you design the program. Keep a log if you choose to.

Referencing the work of another artist isn't required, but is a good way to get inspiration.

## Submission

Submit to Canvas:

- Your `homage.py` program and one of its output images
- Your original program and *three* of its output images
- Your AI log if you used one
