# CYOA

## Schedule

This is the lab for week 8. Lab 7 was replaced by the hurricane assignment.

## Overview

We have a variety of projects in this lab:

- Implementing a Choose Your Own Adventure Story. This doesn't introduce any new content, but will allow you to practice structuring a larger program using functions.
- Modeling a deck of cards using a list.
- Writing a mini-ChatGPT using the **OpenAI API**.

## Setup

Create a `Lab_8` directory and `cd` into it:
```
mkdir Lab_8
```
```
cd Lab_8
```


## Choose Your Own Adventure


<img src="https://upload.wikimedia.org/wikipedia/en/f/f0/Cave_of_time.jpg" width="25%" />


If you had been a kid in the 80's, your elementary school library would have been stuffed with *Choose Your Own Adventure* books, for the downtime you had when you weren't playing [*Oregon Trail*](https://en.wikipedia.org/wiki/The_Oregon_Trail_(1985_video_game)) on your school's Apple II computers.

Each book was the story of "you", the nameless protagonist, making your way through some type of fantastic adventure story. After reading for a few pages, you'd be offered a choice. For example,

- *If you choose to explore the mysterious Cave of Time, turn to page 41*.
- *If you would rather go back to your house and make a sandwich, go to page 17*.

Each choice would lead to a different path of the story and eventually you would reach an ending page, which might good, bad, or ambiguous.

We're going to use Python to write our own text-based Choose Your Own Adventure story. A key idea of this program will be **using functions to organize a complex program**. Each "page" of the story will be its own function. Within each function, print a little descriptive text, then prompt the user to make a choice. 
Each choice corresponds to another function call, which runs the code for the next page.

### Interactive Fiction

<img src="https://upload.wikimedia.org/wikipedia/en/a/ac/Zork_I_box_art.jpg" width="200px" />

*The Zork series published by Infocom was an influential early computer game. It is pitch black. You are likely to be eaten by a grue.*

<br/>

The CYOA books are part of the larger gaming lineage of **interactive fiction**. Some of the earliest PC games were structured as interactive stories, where the player types commands to move around the world, gather items, and solve puzzles. These early text-based IF games later evolved into graphical adventure games.

IF is kind of a weird genre. It's both totally unpopular and extremely popular at the same time. There are still writers creating interesting parser-based IF in the 
style of the early text adventure games: Modern IF in this style is often experimental or socially-conscious. Basically none of that crosses over to the commerical gaming market. On the other hand, there is huge genre of visual novel games, dating sims, and other text-and-image games that have achieved widespread popularity, even if they often get tagged as "casual" or "romance" games.

While I'm certainly **not** a connossieur of the form, many of these games are gloriously weird.

<img src="https://cdn.akamai.steamstatic.com/steam/apps/251990/ss_267dc852c216b2bf58d48c58f3ea31d6896e19e4.1920x1080.jpg?t=1568494485" width="300px" />

*Long Live the Queen*, a dark and gritty stats-based princess simulator where you have to train skills that will allow you to survive until your coronation.

<img src="https://hips.hearstapps.com/digitalspyuk.cdnds.net/14/25/gaming-hatoful-boyfriend-screenshot-2_1.jpg" width="300px" />

*Hatoful Boyfriend*, the dating sim game where the guys you're trying to date just happen to be pigeons.

<img src="https://i.pcmag.com/imagery/articles/03vQmmuNtMgqoVDDHYMhunN-1.1569489919.fit_lim.png" width="300px" />

*I Love You, Colonel Sanders*, the KFC-themed dating simulator. Colonel *senpai*, notice me!


### An example story

Create a new file named `cyoa.py`. Copy the following code then run it a couple of times to see how it works. Once you have played through a few paths, trace the execution of the source code and verify that you understand how it works.

```
"""
A Choose Your Own Adventure Story
"""

def read_choice():
    """
    Read and return an integer value
    """
    return int(input('Make a choice: '))
    

def go_to_house():
    
    print()
    print('Congratulations! You made back to your house!')
    print('If only there was some way to get inside...')
    print()
    
    # Add some more choices
    # Each choice corresponds to a function that represents the next page in the story
   
   
def read_leaflet():

    print()
    print('The leaflet turns out to be a coupon for a nearby all-you-can-eat buffet.')
    print('Your stomach rumbles...')
    print('But you need to head back to your house before you do anything else.')
    print()
    
    # Go directly to the next page without offering a choice
    go_to_house()

    
def open_mailbox():
    
    print()
    print('Opening the mailbox reveals a small leaflet.')
    print()
    
    print('1. Read the leaflet.')
    print('2. Change your mind and go to the house.')
    
    choice = read_choice()
    
    if choice == 1:
        read_leaflet()
    else:
        go_to_house()
        

def start():
    
    print()
    print('You are standing in an open field west of a white house with a boarded front door.')
    print('There is a small mailbox here.')
    print()
    
    print('1. Go to the house.')
    print('2. Open the mailbox.')
    
    choice = read_choice()
    
    if choice == 1:
        go_to_house()
    else:
        open_mailbox()
        
        
def print_instructions():
    
    print('Welcome to my Choose Your Own Adventure story!')
    print()
    
    print('Every page in this book is implemented as a function.')
    print('On each page, you\'ll make a choice, which calls the next function.')
    print('Let\'s begin!')
        
        
### Main
print_instructions()
start()
```

### Structure of the Program

The `main` part calls two functions: `print_instructions`, which just prints an intro message and then returns, and `start`, which is
the first page of the story.

The `start` function prints a little description of the scene and then prompts the user to choose option 1 or 2, reading the choice
with the `input` function.

Each choice corresponds to another function: `go_to_house` or `open_mailbox`. If the user makes choice 2, for example, the program calls the `open_mailbox` function, which represents another page in the story with another set of choices.

Here's a key idea: within `start`, we're using functions to **describe what should happen next**. Each function represents one self-contained page with calls to the functions representing other pages. Thus, the code is nicely compartmentalized. In particular, **we could change the code for one page without having to rewrite any other page**.

### Your Mission

Once you're comfortable with the basic example story, take control and write your own. You can use the starter code as a model and either keep the same opening scenario and choices or write something completely different.
Here's the basic plan:

- Use the `start` function as a model for all of your functions.

- Each function prints some text of the story, then prints some choices. You can do 1, 2, 3, or more choices, depending on how you want
the story to develop.

- Read the number for the user's choice with the `read_choice()` function. You can assume the user will always put in a valid number.

- For each choice, call a function that decribes what you want to happen next.

- Then go write those methods to create the next pages of the story.


## Cards Revisited

### Suits and ranks

Previously, we used `randint(1, 13)` to simulate dealing a playing card. This worked, but gave uniform probabilities for every card, which isn't the same as dealing out of a real deck.

Let's use a list to model the actual deck of 52 cards. Represent each card as a number 0 to 51.

- The first 13 cards (numbered 0 to 12) will be the clubs
- The next 13 (numbered 13 to 25) will be the diamonds
- And so forth for the diamonds and then the spades

Given a card's number you can map it to the corresponding suit by dividing by 13:
```
def suit(card):
    """
    Convert a card id to its given suit
    """

    # List of all suits
    SUITS = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']

    # Dividing by 13 gives 0 if the card is a club, 1 for diamonds, etc.
    suit = card // 13

    return SUITS[suit]
```

Put the code below in `cards.py`, then complete the `rank` function that takes a card number as input and returns its associated rank. Tip: think about using the mod operator.
```
"""
Simulating a deck of 52 playing cards
"""

from random import shuffle

def suit(card):
    """
    Convert a card id to its given suit
    """

    # List of all suits
    SUITS = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']

    # Dividing by 13 gives 0 if the card is a club, 1 for diamonds, etc.
    suit = card // 13

    return SUITS[suit]


def rank(card):
    """
    Given a card's number, return its associated rank
    """

### Main

# Create a list of numbers 0 to 51
deck = list(range(52))

# Built-in shuffle method permutes the list
shuffle(deck)

# Print the cards
for card in deck:
    print(rank(card) + ' of ' + suit(card))
```

### Simulating blackjack

Now use your fancy new deck to simulate the probability of dealing a blackjack from the first two cards in a freshly shuffled deck.

- Use a loop to run a large number of trials
- On each trial, generate and shuffle a new deck, then check the first two cards
- If one card is an Ace and the other is a Ten or face card, then it's a blackjack
- Keep track of the number of trials that yield blackjacks

```
### Main

blackjacks = 0

# Run a large number of simulated trials
for trial in range(1000):
    # Generate and shuffle a new deck

    # Check the first two cards and see if they're a blackjack

    # If so, increment the success counter


# Print the fraction of trials that yielded a blackjack
```

## Using the OpenAI API

### Description

Let's practice interacting with the **OpenAI API**.

You're familiar with using an AI model through a chat interface, like ChatGPT. It's also possible to **call the model directly from a program**. That is, rather than typing a prompt into a chat box, submitting it, and receiving the chat answer, you can incorporate calls to the GPT model directly into your Python code. This is the approach you would take if you were building an application that used LLM capabilities behind the scenes.

GPT is too computationally intensive to run on your local computer, so when you want to interact with it, you send a request over the Internet to OpenAI, containing the prompt that you want GPT to use. The request is processed in their datacenters and the response is returned to you over the Internet. Once your program receives the request, you can unpack it and use it in whatever way makes sense for your application.

OpenAI has [a published specification](https://platform.openai.com/docs/api-reference/introduction) for how developers can submit requests to their services and receive the responses. The specs define what kinds of services OpenAI makes available, how requests to those services should be formatted, and so forth. This set of specs is called an **Application Programming Interface** (API). 

APIs are a key element of modern programming, because they allow application developers to access specialized services provided by remote companies. 

Other major cloud-based companies also provide APIs to allow programmers to interact with their services. For example, if you were developing a program that needed to interact with Instagram data you would use the [Instagram API](https://developers.facebook.com/products/instagram/apis/).


### Secret API key

To use the OpenAI service, you need to have a special, secret **API key** that allows OpenAI to associate your requests with a particular account. I've already created that API key and e-mailed it to you before class.

The key is used to manage billing for our class account, using a pool of credits that I've already set up and paid for. Practically, the risks of misuse are low (I'm the owner of the account and I have billing limits set), but let's practice some basic information security:

- Do not forward the key to anyone
- Don't store the key in clear text in any file on your GitHub codespace

First, you need to put your key into your terminal as an **environment variable** so that it can be used by your programs. Type the following **in the terminal**. 
```
export OPENAI_API_KEY="PASTE THE REAL KEY IN BETWEEN THESE QUOTES"
```
Paste the key into the specified spot, then press ENTER. You can check that the environment variable was successfully created using
```
printenv OPENAI_API_KEY
```
You should see the key you just pasted printed back out.

This way of storing the key only persists for one terminal session, so if you log out, you'll have to repeat the `export` commmand when you log back in. There are ways to store the API key in more durable ways (including as an encrypted secret), but those are more complex so we're going to avoid them for now.

### Install the `openai` module

Next, you need to install the `openai` module, which provides functions for handling API requests. In your terminal type:
```
pip install openai
```
`pip` is the *Package Installer for Python*, a standard tool for loading new packages that aren't already installed on your system.

### Code
Now create a file named `chat.py` and put the following code inside it:
```
"""
Using the OpenAI API

Borrowed from the official documentation
"""
from openai import OpenAI
client = OpenAI()

# client.chat.completions.create is the basic function to submit a request
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about AI."
        }
    ]
)

# Print the response
print(completion.choices[0].message.content)
```
Run the program. You should see it print out a short poem. Run it a few more times.

### User and system prompts

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sepia_officinalis_%28aquarium%29.jpg/1920px-Sepia_officinalis_%28aquarium%29.jpg" width="300px" />

*The common cuttlefish, *Sepia officinalis*, via Wikipedia*

<br/>

The primary routine to submit a chat request is `client.chat.completions.create`. It takes two parameters:

- `model`, the name of the model the request should use. For us, this will **always** be `"gpt-4o-mini"`. The 4o-mini model is a good balance of performance and cost.
- `messages`, a list of inputs that describe the prompt the chat should execute.

The inputs to messages are two collections of key-value pairs enclosed in curly braces. Technically, these are Python dictionaries, which we'll discuss in more detail soon.

The first set of key-value pairs specifies the **system prompt**. This is typically used to give the model a role or supply it with relevant background information and guidelines. The second is the **user prompt**, which is the actual request. This is what you would type into the chat box in a regular ChatGPT interaction.

Try changing the system prompt to the following, then re-run your program and see how the response changes:
```
{"role": "system", "content": "You are a helpful assistant. You are fascinated by cuttlefish and try to incorporate references to them into your responses."},
```


### Jam

Now experiment with changing the prompt, asking some different questions, and printing the responses out. You can modify the system prompt to give the bot roles or guidelines.


### Temperature

The chat call can take a few more parameters that control the model. An important one is **temperature**, which controls the amount of randomness in the model's next-token predictions.

Temperature can be a value from 0 to 2.

- Lower temps make responses more predictable; the model is more likely to choose the most probable next token at each step
- Higher temperatures introduce more variability into the output, at the risk of making the next-token predictions incoherent

The default temperature is .7.

Experiment with adding the `temperature` value to the function call. Repeat some prompts and see how the reponses vary as you change temperature.
```
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about AI.",
        }
    ],
    temperature=.7
)
```


## Do-It-Yourself ChatGPT


### Basic chat

Let's make our own terminal-based version of ChatGPT. The flow for version one is simple:

- In the main part of the program, prompt the user to enter a request
- Call the chat routine to process that request and print the response

Take a look at this version. It's almost the same as what we had before, except the chat interaction is now wrapped in a function and takes the `user_message` as an input parameter.
```
"""
Example interactive chat using the OpenAI API
"""

from openai import OpenAI
client = OpenAI()

def chat_request(user_message):
    """
    Send the given user message to GPT and print the response
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    print()  # Blank line
    print(completion.choices[0].message.content)


### Main

# Prompt the user to enter a message
user_input = input('\nI\'m a helpful assistant. Enter your request:\n\n')

# Call chat and print the response
chat_request(user_input)
```

### Loop

Let's add a loop around the basic chat.

The `while` loop tests a boolean condition and repeats as long as that condition evaluates to `True`. The simplest `while` loop is `while True`, which repeats the body of the loop infinitely until the program terminates or a condition triggers to break out of the loop.
```
while True:
    # Repeatedly execute the body of this loop forever 
```

Here's a variation of the chat program that wraps the user input step into a basic `while` loop. It ends if the user types `quit`.

```
### Main

while True:
    # Prompt the user to enter a message
    user_input = input('\nI\'m a helpful assistant. Enter your request or type quit to end:\n\n')

    # If the user types "quit", end the chat
    if user_input.lower() == 'quit':
        break  # Break ends the current loop immediately

    # Call chat and print the response
    chat_request(user_input)
```

Spend a few minutes playing with this chat program. Try making some references to previous prompts. Do they perform the way you would expect?


### Persistence of memory

<img src="https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg" width="300px"/>

*Persistence of Memory*, Salvador Dali (1931)

<br/>

If you experiment, you'll observe that this version of the program stuggles with context, because it isn't actually keeping track of the user's requests or GPT's responses. Each interaction is **stateless** and independent of every other interaction. Therefore, we need to keep track of the state of the conversation as it progresses.

Here's the first version of this approach, which keeps all interactions in one big list named `history`. When it's time to submit a request, we join those individual messages into one huge string, which becomes the input to the chat request.
```
### Main

history = []

chatting = True
while chatting:
    # Prompt the user to enter a message
    user_input = input('\nYou:\n\n\t')

    # If the user types "quit", end the chat
    if user_input.lower() == 'quit':
        break  # Break ends the current loop immediately

    # Add the user's current request to the interaction history
    history.append(user_input)

    # Turn the list of strings into a single string
    #
    # '\n'.join takes a list of strings and concatenates them together,
    # separated by newline characters
    conversation = '\n'.join(history)

    # Call chat on the entire conversation
    response = chat_request(conversation)

    # Print the assistant's response
    print('\nAssistant:\n\t', response)

    # Add the response to the memory
    history.append(response)
```
To use this version, modify the `chat_request` function to **return** the response instead of printing it.

Play with the program. Is it able to reference previous parts of the chat?


### Interactions

We can actually do even better. The API allows you to supply not just a big string with the history of the chat, but an alternating record of the user and assistant interactions. Here's an example from the documentation:
```
  messages: [
    {
      "role": "user",
      "content": [{ "type": "text", "text": "knock knock." }]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "Who's there?" }]
    },
    {
      "role": "user",
      "content": [{ "type": "text", "text": "Orange." }]
    }
  ]
```

Take a look at the following version of the program. It users two lists to keep track of the user input and assistant responses, then shows off a fancier way of combining them into the `messages` list in the chat function.
```
"""
Example interactive chat using the OpenAI API
"""

from openai import OpenAI
client = OpenAI()


def chat_request(user_messages, assistant_messages):
    """
    Chat interaction using both user and assistant histories
    """

    # Starting messages list with system prompt
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    # Append all previous pairs of interactions - this is controlled by the number of
    # assistant reponses
    for i in range(len(assistant_messages)):
        messages.append({"role": "user", "content": user_messages[i]})
        messages.append({"role": "assistant", "content": assistant_messages[i]})

    # Append the most recent user message as the final element of the messages list
    messages.append({"role": "user", "content": user_messages[-1]})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return completion.choices[0].message.content


### Main

user_history = []
assistant_history = []

while True:
    # Prompt the user to enter a message
    user_input = input('\nYou:\n\n\t')

    # If the user types "quit", end the chat
    if user_input.lower() == 'quit':
        break  # Break ends the current loop immediately

    # Add the user's current request to the interaction history
    user_history.append(user_input)

    # Call chat on the entire conversation
    response = chat_request(user_history, assistant_history)

    # Print the assistant's response
    print('\nAssistant:\n\t', response)

    # Add the response to the memory
    assistant_memory.append(response)
```
Implement that program, play with it, then look through the code and verify that you understand how each part works.

