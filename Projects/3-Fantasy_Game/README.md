# Fantasy Game

<img src="narrator.png" width="300px" />

*Ancient storyteller in a fantasy game*, made with DALL-E 3

<br/>

## Due Friday, 10/25

## Overview

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC0Dhs6yR99_mz6DCtuPFB22I5AsGVc51V3TyiYsuqFncgj_2Iw6Cto3wIdhRtUcGB7bIbo1Y804U6ILalWX81jP3zXhyxPlYxgGxxEl513CxdaYVRWAJbt1WZypZ-p265gDWvcTNwp8o/s400/wiztitle.gif" width="300px" />

*Wizardry*, one of the most influential computer games of all time, via [the CRPG Addict blog](https://crpgaddict.blogspot.com/2010/02/game-5-wizardry-proving-grounds-of-mad.html)

<br/>

*Dungeons and Dragons* is the archetypal fantasy roleplaying game, where players take on the roles of adventurers exploring a fantasy world, guided by a "dungeon master" who determines the course of the story and evaluates the results of players' decisions by rolling dice. Lots of dice.

The earliest computer RPGs, like *Wizardry* (1981), borrowed heavily from the basic concepts of D n' D, with the computer taking on the role of the dungeon master. However, computer games always failed to reproduce the truly open-ended worlds of interactive tabletop RPGs, since they were limited by what the designers could code into the game.

Let's jump forward almost 40 years to 2019, when a Brigham Young University student named Nick Walton [created *AI Dungeon*](https://if50.substack.com/p/2019-ai-dungeon). *AI Dungeon* used the then-cutting-edge text generation program ***GPT-2*** to create interactive narratives that could grow and expand over time.

This project will allow you to continue experimenting with the OpenAI API by using it to write your own fantasy exploration game. You will:

- Choose the theme and setting of your game
- Give the player a starting scene and some initial choices
- Prompt GPT to continue the story, generating the next scene or room and more choices for the player

Along the way, you'll get to practice using loops, lists, functions, and the other features we've developed so far.

## AI Usage

Beyond using the API, you can use AI tools to help you develop your ideas and code. As before, keep a log of your AI interactions and your reactions to the AI's responses, so you have a record of how your project developed.

## Setup

Make a `Project_3` directory and create a file named `game.py` inside it.

## Review the basic chatbot

The starting point for this project is the basic chatbot from Lab 8. Review that code and make sure you understand how it's implemented and how to use the OpenAI API before continuing with this project.

## Guidelines

This project is intentionally open-ended. You can choose the setting, themes, etc. based on your interests. If you want to choose something other than a [Standard Fantasy Setting](https://tvtropes.org/pmwiki/pmwiki.php/Main/StandardFantasySetting), you can do that.

Your program should use a `while` loop that repeatedly generates and displays the next scene of the story and offers the player some choices. The player selects a choice and then the game generates the next output. Keep track of the history of the conversation, like in the basic chatbot.

Think about how to prompt GPT. You may need to supply some additional information, in the system prompt or as part of the request, to get it to do what you want.

### Original feature

I want you to add **at least one original feature** to your program that goes beyond the core chat interaction framework. Some ideas:

- Pre-scripted narrative events that occur randomly
- Combat against monsters (or other mini-games) that are triggered randomly, like in a standard computer RPG
- Maintaining a list of items that you can find and then use
- Stats, levels, skills, etc.
- Changing the prompt that goes to the AI over time to change the tone/theme/setting of the game as the player advances

These are just suggestions and you can choose whatever you want, but I want you to be **ambitious** and creative.

## Submission

Submit your `game.py` file and your log of AI interactions to Canvas.

Note that I need the **actual Python script** as a .py file, not a copy of your code pasted into another document.
