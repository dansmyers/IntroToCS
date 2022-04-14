# Graphical Programming with Pygame

<img src="https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67" width="30%" />

## Setup

Create a new Replit workspace using the **Pygame** environment (not the regular Python environment). It may be helpful to use the search bar at the top of the workspace creation window to find the Pygame environment more easily.

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

<img src="http://www.hrwiki.org/w/images/1/18/secretcollectbox.PNG" width="30%" />

A re-implementation of an early game by Videlectrix, makers of classic games like *Awexome Cross*, *Thy Dungeonman*, *RhinoFeeder*, and the *Snake Boxer* series. You are a square that's trying to collect another square. This program will illustrate how to do keyboard input and hit detection.

```
import pygame
pygame.init()

fps_clock = pygame.time.Clock()

black = pygame.Color('black')
white = pygame.Color('white')
blue = pygame.Color('blue')
red = pygame.Color('red')

size = 640, 480

screen = pygame.display.set_mode(size)

# Set keyboard to accept repeats
#
# This allows multiple keypress signals to be sent
# when the user holds down a keyboard key
#
# Parameters control the rate of key events
pygame.key.set_repeat(10, 10)

player_x = 100
player_y = 100
goal_x = 150
goal_y = 150
square_size = 10
step = 2

running = True
while running:
  screen.fill(white)
  screen.fill(blue, (player_x, player_y, square_size, square_size))
  screen.fill(red, (goal_x, goal_y, square_size, square_size))

  # Create two Rect objects for the player and goal positions
  player_rect = pygame.Rect(player_x, player_y, square_size, square_size)
  goal_rect = pygame.Rect(goal_x, goal_y, square_size, square_size)

  # pygame.Rect.colliderect() returns True if the two Rects overlap
  #
  # If the collision test succeeds the loop ends
  if pygame.Rect.colliderect(player_rect, goal_rect):
    running = False

  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Key presses are signified by a KEYDOWN event
    #
    # The pressed key is stored in event.key
    # Eack key is mapped to a constant
    #
    # Pressing a key adjusts the player square's position
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_y -= step
      elif event.key == pygame.K_DOWN:
        player_y += step
      elif event.key == pygame.K_LEFT:
        player_x -= step
      elif event.key == pygame.K_RIGHT:
        player_x += step

  # Update display
  pygame.display.update()
  fps_clock.tick(20)

pygame.quit()
```

Most of the elements are similar to what you've seen before. One new piece is the hit detection code:

```
  # Create two Rect objects for the player and goal positions
  player_rect = pygame.Rect(player_x, player_y, square_size, square_size)
  goal_rect = pygame.Rect(goal_x, goal_y, square_size, square_size)

  # pygame.Rect.colliderect() returns True if the two Rects overlap
  #
  # If the collision test succeeds the loop ends
  if pygame.Rect.colliderect(player_rect, goal_rect):
    running = False
```

The first lines create two `Rect` objects, one for each square. The `colliderect` method then tests if the two `Rect` objects overlap with each
other (that is, if they are in collision). When the player collides with the goal square, the game ends.

The second new piece is keyboard input:

```
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_y -= step
      elif event.key == pygame.K_DOWN:
        player_y += step
      elif event.key == pygame.K_LEFT:
        player_x -= step
      elif event.key == pygame.K_RIGHT:
        player_x += step
```

Triggering a `KEYDOWN` event checks for what key was pressed and then adjusts the player's position accordingly.


## Objectify It

Here is an object-oriented version of the Secret Collect program. As before, the drawing and moving code has been moved into class methods. We've also moved the code to check for collisions into the class. The `check_collision` method takes another square as input and checks if the two overlap using `colliderect`.

```
import pygame
pygame.init()

class Square:
  """
  A class that represents a square on the screen
  """

  def __init__(self, x, y, size, color):
    self.x = x
    self.y = y
    self.size = size
    self.color = color

  def draw(self):
      screen.fill(self.color, (self.x, self.y, self.size, self.size))    

  def check_collision(self, other_square):
    self_rect = pygame.Rect(self.x, self.y, self.size, self.size)
    other_rect = pygame.Rect(other_square.x, other_square.y, other_square.size, other_square.size)    

    return pygame.Rect.colliderect(self_rect, other_rect)

  def move(self, key):
    if key == pygame.K_UP:
      self.y -= STEP
    if key == pygame.K_DOWN:
      self.y += STEP
    if key == pygame.K_LEFT:
      self.x -= STEP
    if key == pygame.K_RIGHT:
      self.x += STEP
      
# Standard setup
fps_clock = pygame.time.Clock()

black = pygame.Color('black')
white = pygame.Color('white')
blue = pygame.Color('blue')
red = pygame.Color('red')

size = 640, 480
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(10, 10)

STEP = 2

# Create two Square objects, one for the player and one for the goal
player = Square(100, 100, 10, blue)
goal = Square(150, 150, 10, red)

# Main loop
running = True
while running:
  screen.fill(white)

  player.draw()
  goal.draw()

  # Check ending condition -- Rect test is now moved to a class method
  if player.check_collision(goal):
    running = False

  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      player.move(event.key)

  # Update display
  pygame.display.update()
  fps_clock.tick(20)

pygame.quit()
```

# PONG

<img src="https://www.gamasutra.com/db_area/images/feature/3900/0401.png" width="30%"/>

The grandaddy of them all.

```
"""
PONG
"""

import pygame
from pygame.locals import *

class Paddle:
  """
  A paddle controlled by the user

  Attributes:
    x, y = the upper left corner of the paddle
    width, height = the extent of the paddle
  """

  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def draw(self):
    screen.fill(black, (self.x, self.y, self.width, self.height))

    

class Ball:
  """
  The Pong ball

  Attributes:
    x, y = ball center
    dx, dy = ball velocity
    r = ball radius
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
    """
    Move this ball, reflecting off the top or bottom edge if necessary
    """
    self.x += self.dx
    self.y += self.dy

    # The ball can only reflect off of the top or bottom edge
    if self.y + self.r >= screen.get_height() or self.y - self.r < 0:
      self.dy = -self.dy

  def test_paddle_reflection(self, p):
    """
    Test if this ball intersects with a paddle

    Input:
      p = the paddle

    Returns:
      Nothing
    """
    
    # A rectangle that encloses the ball
    self_rect = Rect(self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r)

    # A rectangle that encloses the paddle
    paddle_rect = Rect(p.x, p.y, p.width, p.height)

    # If the ball intersects the paddle, reflect the ball in the x direction
    if self_rect.colliderect(paddle_rect):
      self.dx = -self.dx

  def at_edge(self):
    """
    Return True if this Ball has reached the left or right edge of the screen
    """
    return self.x - self.r < 0 or self.x + self.r >= screen.get_width()

    
#--- Setup
    
# Initialize pygame
pygame.init()

# Clock object
fps_clock = pygame.time.Clock()

# Colors
black = pygame.Color('black')
white = pygame.Color('white')

# Screen
size = 320, 240
screen = pygame.display.set_mode(size)

# Key repeats
pygame.key.set_repeat(10, 10)

STEP = 2

# Create paddles and ball
left_paddle = Paddle(0, 100, 10, 40)
right_paddle = Paddle(310, 100, 10, 40)
ball = Ball(100, 100, 5, 2, 2)

#--- Main loop
running = True
while running:

  # Clear the screen
  screen.fill(white)

  # Call draw methods
  left_paddle.draw()
  right_paddle.draw()
  ball.draw()

  # Move the ball, checking reflections
  ball.move()
  ball.test_paddle_reflection(left_paddle)
  ball.test_paddle_reflection(right_paddle)

  # Test for ending condition
  if ball.at_edge():
    running = False

  # Check events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.KEYDOWN:

      # Up and down keys move right paddle
      if event.key == K_UP:
        right_paddle.y -= STEP
      if event.key == K_DOWN:
        right_paddle.y += STEP

      # w and s keys move the left paddle
      if event.key == K_w:
        left_paddle.y -= STEP
      if event.key == K_s:
        left_paddle.y += STEP

  # Update display
  pygame.display.update()
  fps_clock.tick(20)

pygame.quit()
```

