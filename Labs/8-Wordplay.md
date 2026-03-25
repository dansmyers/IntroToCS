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



## Using the OpenAI API

### Description

Let's practice interacting with the **OpenAI API**.

You're familiar with using an AI model through a chat interface, like ChatGPT. It's also possible to **call the model directly from a program**. That is, rather than typing a prompt into a chat box, submitting it, and receiving the chat answer, you can incorporate calls to the GPT model directly into your Python code. This is the approach you would take if you were building an application that used LLM capabilities behind the scenes.

GPT is too computationally intensive to run on your local computer, so when you want to interact with it, you send a request over the Internet to OpenAI, containing the prompt that you want GPT to use. The request is processed in their datacenters and the response is returned to you over the Internet. Once your program receives the request, you can unpack it and use it in whatever way makes sense for your application.

OpenAI has [a published specification](https://platform.openai.com/docs/api-reference/introduction) for how developers can submit requests to their services and receive the responses. The specs define what kinds of services OpenAI makes available, how requests to those services should be formatted, and so forth. This set of specs is called an **Application Programming Interface** (API). 

APIs are a key element of modern programming, because they allow application developers to access specialized services provided by remote companies. Other major cloud-based companies also provide APIs to allow programmers to interact with their services. For example, if you were developing a program that needed to interact with Instagram data you would use the [Instagram API](https://developers.facebook.com/products/instagram/apis/).


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

