# Graphical Programming with Pygame

## Setup

## First Program

The first program illustrates how to initialize Pygame, create a window, and draw a solid-colored rectangle onto it. Pygame programs require a little bit of boilerplate code to get them set up, but nothing that's too hard for us to understand at this point.

**Type** the following program into your Repl.it workspace. The comments explain what each line is doing.

```
"""
Initialize a window and draw onto it
"""

# Import pygame and call init -- do this before anything else
import pygame
pygame.init()

# Create a clock object -- used to control frame rate
fps_clock = pygame.time.Clock()

# Load color constants
blue = pygame.Color('blue')
red = pygame.Color('red')

# Define the window size
# width, height in pixels
size = 320, 240

# Initialize the screen
screen = pygame.display.set_mode(size)

# Main loop -- eventually game logic will go in here
running = True
while running:

  # Put a rectangle on the screen
  #
  # The tuple (100, 50, 150, 25) means a rectangle with its
  # upper-left corner at position (100, 50), a width of 150
  # and a height of 50
  #
  # UNEXPECTED: Position (0,0) is in the UPPER-LEFT CORNER!
  screen.fill(blue, (100, 50, 150, 25))

  # Call display.update to make screen changes take effect
  pygame.display.update()

  # Pygame automatically collects events that happen on the screen
  #
  # QUIT is triggered when the user closes the window
  #
  # This section will eventually include handling keyboard and
  # mouse input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Pause long enough to run at 10 frames per second
  fps_clock.tick(10)

pygame.quit()
```

The basic program sets up a screen of size 320 pixels wide by 240 pixels high, then runs the main game loop. The loop repeatedly draws a blue rectangle with its upper-left corner at position (100, 50). **Click the X in the upper right of the Pygame window to trigger the QUIT event and end the program**.

Here's a key point: the coordinate system has position (0,0) in the **upper-left corner**, not the bottom-left like you would expect from normal graphing. It's helpful to think of coordinates as "over and down" rather than "over and up" like on a normal x-y plane.

Experiment with changing the color, position, and size of the rectangle before you move on.

## Blink

The first program had all of the basic elements in place, but just drew one static rectangle. Let's modify it to a blinking rectangle that changes color on each frame. Update the main loop to the following:

```
# Main loop
screen_state = 0
running = True

while running:

    # Draw the colored rectangle -- switch color every frame
    if screen_state == 1:
        screen.fill(blue, (100, 50, 150, 75))
        screen_state = 0
    else:
        screen.fill(red, (100, 50, 150, 75))
        screen_state = 1
        
    # Event-handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Update the display, then pause for frame rate
    pygame.display.update()
    fps_clock.tick(10);
    
pygame.quit()
```

## Ball

Let's add some movement. **Type** in the program below to implement a bouncing ball screen saver.

```
"""
Follow the bouncing ball
"""

import pygame
pygame.init()

# Create a clock object -- used to control frame rate
fps_clock = pygame.time.Clock()

# Load color constants
black = pygame.Color('black')
white = pygame.Color('white')

# Define the window size
size = 320, 240

# Initialize the screen
screen = pygame.display.set_mode(size)

# Set the ball's position and radius
ball_x = 100
ball_y = 50
ball_r = 20

# Main loop
state = 0
running = True

while running:

  # Clear the screen
  screen.fill(white)

  # Draw the ball
  pygame.draw.circle(screen, black, (ball_x, ball_y), ball_r)

  # Event-handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update and pause
  pygame.display.update()
  fps_clock.tick(10)
```

The program should be clear given the previous examples. The only difference is that we're now drawing a circle to a position controlled by the variables `ball_x` and `ball_y`.

Let's add some animation. Put in two more ball variables to control the ball's velocity:

```
ball_dx = 2
ball_dy = -3
```

Now add the following code to the main game loop. Put it after the line that draws the circle but before the event handling loop:

```
# Move the ball
ball_x += ball_dx
ball_y += ball_dy

# Check for reflection off the edge -- if so, reverse velocity direction
if ball_x + ball_r >= screen.get_width() or ball_x - ball_r <= 0:
  ball_dx = -ball_dx
  
if ball_y + ball_r >= screen.get_height() or ball_y - ball_r <= 0:
  ball_dy = -ball_dy
```

Animation is simply implemented by changing the positions of elements so that they get drawn in new locations on each iteration. Play around with changing the starting position, size, and velocity. If you think the movement is a little jerky, try increasing the framerate, which may require reducing the velocity to get the speed you want.


## Object-Oriented Ball

Consider this: how many variables are required to describe a single ball in motion? At least five (x, y, radius, dx, and dy), and maybe more if we wanted to incorporate color as a variable. What would you do it you wanted to add multiple balls to the program above, or combine a moving ball with other on-screen elements.

Also, consider how code that changes the state of the ball (moving, reflecting, etc.) is mixed in with the main loop's code.

Object-oriented programming can provide a solution to these problems: grouping related variables together as a unit and separating code that draws and controls each on-screen element from other code.

Here's an object-oriented version of the ball program. The `Ball` class at the top defines three methods:

- A `__init__` constructor that sets the position, size, and velocity of the ball
- `draw`, which uses pygame methods to put the `Ball` on the screen
- `move`, which updates the Ball's position in an appropriate way.

The main loop now contains only calls to `ball.draw()` and `ball.move()`.

```
import pygame
pygame.init()

class Ball:
  """
  A class representing a ball
  
  Key idea: the Ball contains variables representing all of its properties
  """
  
  def __init__(self, x, y, r, dx, dy):
    self.x = x
    self.y = y
    self.r = r
    self.dx = dx
    self.dy = dy

  def draw(self):
    pygame.draw.circle(screen, black, (self.x, self.y), self.r)

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x + self.r >= screen.get_width() or self.x - self.r < 0:
      self.dx = -self.dx

    if self.y + self.r >= screen.get_height() or self.y - self.r < 0:
      self.dy = -self.dy


# Standard setup
fps_clock = pygame.time.Clock()

black = pygame.Color('black')
white = pygame.Color('white')

size = 320, 240
screen = pygame.display.set_mode(size)

# Construct a Ball object
ball = Ball(100, 100, 10, 1, 1)

# Main loop
running = True
while running:
  screen.fill(white)

  ball.draw()
  ball.move()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()
  fps_clock.tick(20)

```

After you implement the first version, try adding multiple `Ball` objects. Construct a new `Ball`:

```
ball2 = Ball(FILL IN STARTING PARAMETERS HERE)
```

Then call `ball2.draw()` and `ball2.move()` in the main loop.


## Secret Collect.






