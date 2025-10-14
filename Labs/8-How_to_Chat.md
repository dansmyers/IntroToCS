# How to Chat

<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Comete_Tapisserie_Bayeux.jpg" width="400px" />

*Detail of Halley's Coment in the [Bayeux Tapestry](https://en.wikipedia.org/wiki/Bayeux_Tapestry) (late-11th Century)*

<br/>


## Overview

This lab will help you get back into practice with lists and loops. The second part introduces a new technique that we'll use in a future project: Writing a mini-ChatGPT using the **OpenAI API**

## Setup

Create a `Lab_7` directory in your workspace and `cd` into it.
```
mkdir Lab_7
```
```
cd Lab_7
```
The questions will tell you how to create and name your Python scripts.

## Loop practice

### Classical Fibonacci

We've previously used Binet's formula to calculate terms in the Fibonacci sequence. Write a program that uses a loop to calculate and print the first 50 Fibonacci numbers. Put your code in a file named `fib.py`.

Tip: Use two variables `fib_1` and `fib_2` to keep track of the two previous numbers in the sequence. On each loop iteration, calculate the next Fibonacci number, then update the values of `fib_1` and `fib_2`.

```
# First two numbers
fib_1 = 0
fib_2 = 1

print(fib_1)
print(fib_2)

# Calculate 48 more numbers
for i in range(49):
    # Use fib_1 and fib_2 to calculate the next number

    # Print the next number

    # Update fib_1 and fib_2 for the next iteration
```


### Sum of a list

Suppose you have a list of numbers and want to calculate their sum. One way to do this is with the built-in `sum` function:
```
# Example list
a = [2, 3, 5, 7, 11, 13, 17]

# Built-in sum
total = sum(a)
```
Write another implementation that uses a `for` loop to manually calculate the list sum.


### I've got 99 numbers, but I don't know which ones
Here's a popular interview question with a "clever" solution: You're given a list that contains 99 of the numbers 1 to 100 in an unknown order. Determine the one value that's missing.

The "clever" solution is to calculate the sum and then subtract from the expected sum of all numbers 1 to 100. The sum of the integers 1 to `n` is
```
sum_1_to_n = n * (n + 1) / 2
```

Write a program that implements this solution to the problem.
```
"""
Find the missing numbers
"""

from random import shuffle

# Create a list of the numbers 1 to 100
numbers = [i for i in range(1, 101)]

# Randomly order, then remove the first item
shuffle(numbers)
removed = numbers.pop(0)

### Add your code here to find the removed number

# Print the answer
print(removed)

```

### List comprehensions

The previous problem showed an example of initializing a large list in a single line.
```
numbers = [i for i in range(1, 101)]
```
This statement use the `for` loop to iterate through the given range of numbers 1 to 100, and collects each value of `i` into a list. The result is a list containing the values `[1, 2, 3, 4, ... , 100]`.

This technique is called a **list comprehension**. It's a preferred Python technique for initializing lists.

You can use comprehensions to generate different kinds of lists. For example, to generate list of 0/1 coin flips you could write
```
flips = [round(random()) for i in range(100)]
```
The loop runs 100 times. Each iteration generates a random value from 0.0 to 1.0 and then rounds it to either 0 or 1. The result is a list of 100 values that are either 0 or 1. For example, `[0, 0, 1, 0, 1, 1, 1, 0, ...]`.

Use the interactive Python terminal to write list comprehensions to generate the following. Enter each command in the terminal and check the output. You don't need to write a script for this problem.

- A list of the numbers  1 to 25

- A list of the numbers -10 to 10

- A list of the even numbers 2, 4, 6, 8, ... 100

- A list of the values .01, .02, .03, .04, ..., .98, .99. Tip: think about looping from 1 to 100 and then dividing each value of `i` by 100.

- A list of 10 boolean values that are all `False`

End the interactive terminal by pressing CTRL + d.


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

Take a look at this version. It's almost the same as what we had before, except the chat interaction is now wrapped in a function and takes the `user_message` as an input parameter. You can update your `chat.py` file to this version.
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
    assistant_history.append(response)
```
Implement that program, play with it, then look through the code and verify that you understand how each part works.
