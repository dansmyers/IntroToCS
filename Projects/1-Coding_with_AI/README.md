# Project 1: Image Filters with AI

<img src="https://dansmyers.github.io/cute_yarn_robot.jpeg" width="400px" />

*Cute yarn robot, made by my son using DALL-E 3*

## Due Friday, 9/13

## Overview

This is it: the first project. We're going to extend the work you've done so far in class and labs by adding **AI programming** to your set of tools. This project is designed to show off several ways that you can use AI to support your coding, without simply asking an AI to write an entire program for you.

The assignment has two parts:

1. Practice using AI to improve your code, debug errors, and suggest alternatives.

2. Implement photo filters with **Pillow**, a Python image processing library. The goal of this part is to demonstrate how you can use AI to understand and work with unfamiliar libraries and execute your own vision.

For both parts, you'll maintain a **logbook** to record your interactions with AI and your evaluations of its code. This is a key part of the assignment. **I will review your logs to make sure that you're thinking carefully and creatively**. Make sure that your log shows that you're reading the AI's output carefully and thinking critically about it.

At the end of this project, you should feel more comfortable using AI to get suggestions on your work and get unstuck.


## Warm-up Questions

### Setup

Create a Word document named `warmup.doc`. As you complete the questions below, you'll copy your prompts, the AI's responses, and your own evaluations into the document. Remember that the document is there to help you document your thinking process.

Make a new folder called `Project_1` in your codespace. First make sure that you're in your top-level home directory `codespaces-blank`, then run the command
```
mkdir Project_1
```
Change to the project directory:
```
cd Project_1
```
Put all of your code for the project into this directory. At the end, I'll ask you to submit some of your files.


### Improving an Existing Program

Start with the file `smoots.py` in this directory. It uses all of the techniques we've discussed in the first two weeks of class (input, variables, formatted printing) to implement the Smoots converter that we've seen before, but the style is poor.

In your document, analyze this program. Explain what style elements in should have, but doesn't. How would you improve it? You don't need to rewrite the entire program, but provide an overview of the corrections that should be made.

**After you have done that** (not before), go to your AI. Ask it to provide commentary on the program using the following prompt:

*Take a look at the following Python program, which implements a unit converter using input, variables, and printing.*<br/>
*[PASTE PROGRAM HERE]* <br/>
*Act as a code reviewer and identify ways to improve its style. Don't rewrite the program or suggest any changes to its behavior, just give me a list of suggested style improvements.*

Read the AI's output and copy it into your log, then provide your own assessment of ChatGPT's suggestions. Do they agree with the ones you made at the start? Did ChatGPT suggest anything you didn't? Do you *disagree* with any of ChatGPT's suggestions?

Prompt your AI to implement the changes. Copy the revised program into your log, then add a few thoughts on what, if anything, you would modify from the AI's output. For example: Are the comments useful? Are the variable names clear? Is it too wordy?

### Unimproving an Existing Program

You're now going to experiment with adding an error to a program and using AI to find and fix it. Start with the file `binet.py` in this directory, which implements Binet's formula. Copy it into your workspace, run it, and verify that it works correctly.

Do the following steps in your logbook:

- Describe, in words, the error that you're adding to the program. What lines are you changing, and what problem will that create?
- Paste your modified code with the error into you log.
- Run the modified program and paste the error message that you get into the log. Make sure that this is the error you expected.

Prompt your AI to find and fix the error:

*I'm writing the following Python program*<br/>
*[PASTE PROGRAM HERE]*<br/>
*I received the following error message when I ran the program:*<br/>
*[PASTE ERROR MESSAGE HERE]*<br/>
*Explain the error and suggest corrected lines of code to fix it. Don't rewrite the complete program for me, just give me the statements that need to be fixed.*

Copy our AI's output to your document, then check its fix. Does it fix the problem?

### Keep Making Things Worse

Repeat the previous section **two more times**, following the same steps, but choosing different errors for each step. Log all of your writing and responses in `warmup.doc`.

### Suggesting Alternatives

Use the original version of `binet.py`. Ask your AI to suggest an alternate implementation of the same functionality.

*Examine the following program and suggest an alternate way of implementing the program while maintaining the same functionality.*<br/>
*[PASTE PROGRAM HERE]*

Paste the AI's feedback into your log, then give your own assessment of its alternative implementation. There is no specific answer here, but you might want to consider:

- Is it correct? How can you tell?
- Does it have the same functionality, or did the AI add or remove features?
- Did it make only cosmetic changes, or was it able to fundamentally change the logic?
- Did it use langauge features that we haven't learned yet? If so, try modifying the prompt to exclude them.
- Overall, do you find any advantages to ChatGPT's version compared to the original version?


## Image Filtering

<img src="https://taplink.st/p/0/8/f/c/44061182.jpg?0?0" width="400px" />
<img src="https://taplink.st/p/5/0/e/f/44061419.jpg?0?0" width="400px" />

*An example of Instagram's Juno filter, which adds a warming effect by increasing reds and yellows and also increases contrast. [Go here](https://taplink.at/en/blog/how_to_use_instagram_filters_and_where_to_find_them.html) for more side-by-side examples of popular Instagram filters.*

### Overview

In the second part of the project, you're going to experiment with some image processing using a Python library called **Pillow**. The Pillow library is an interface to PIL, the *Python Image Library*, and supports a large number of standard image manipulation algorithms.

The overall goal of this section is to allow you to practice using AI to interact with a library. We haven't talked about Pillow in class but, as you'll see, you can leverage your AI collaborator to use it effectively.

A key to this section is **having opinions**. In several places, you'll be asked to provide as assessment of the AI's output images and suggest ways of improving them. Think about what looks good and what kind of effect you'd like to see.


### Setup
Create a logbook document named `filters.doc`.

Copy `monochrome_filter.py` and `warm_filter.py` to your `Project_1 directory. You can do this by making new files with `touch`, then copying the code into each file.

Download the `cute_yarn_robot.jpeg` image (made by my son using DALL-E 3) and then upload it to your codespace. You can upload by dragging the file into your file browser panel, then dragging it into the `Project_1` directory.

Finally, go into your terminal and run the command
```
pip install Pillow
```
`pip` is the *package installer for Python*, a way to add new libraries to your Python environment. If you don't already have Pillow installed as part of your codespace, the pip command will install it for you.

### Monochrome filter
Open and run `monochrome_filter.py`. It will produce a file named `monochrome_output.jpeg` that contains a grayscale version of the example image.

Take a look at the code. There are several things going on here that are not *too* difficult to undertand, but that we haven't talked about yet. Get some help from your AI: paste the program into your chat and ask the AI to explain what each line does. Copy the prompt and output into your log document.

Add comments to your log about this explanation. Do you have follow-up questions? If so, ask them and include the responses in the log.

### Color images

An image is, fundamentally, a rectangular grid of pixels, where pixel is a number representing the intensity of light measured at that position.

Color images are composed of three **channels**, representing the intensities of red, green, and blue light that make up each pixel. The blend of RGB values for a given pixel determines its specific color and qualities.

Ask your AI to give you more information on RGB colors in images.

*I'm learning about image processing. Can you give me some information on the RGB color model as how it's used in digital images? Include some examples of how different red, green, and blue mixtures can correspond to different colors in the visible image.*

Log the prompt and response in your document.

### Warm and cool filters

Then, look at and run `warm_filter.py`. It implements a filter that emphasizes the red and yellow tones of the image, while slightly de-emphasizing the cooler blue component. Experiment with changing the specific numbers in the filter and observe how that changes the output image. 

Paste the code into your AI and ask it for an explanation of how the warm filter is implemented. Again, paste the response in your log document.

Once you understand the warm filter, make a new file named `cool_filter.py`. Copy the warm filter code, then modify it to create a cool version.


### Vintage filter

Let's make a vintage-style filter that gives the image an effect like an old film photograph. Make a new file named `vintage_filter.py`.

Prompt the AI to modify the warm filter program and produce a vintage-style filter. Log your prompt and the response you get in your document. Include, in your own words, a brief summary of how the filter works. Remember that you can ask for clarification of any lines that don't make sense.

Now run the program and look at the output. What kind of "vintage" did you get? Is it like an old-time sepia-tinted photograph, like a 1980's Polaroid, or something else? In your log, give an assessment of the filter and describe some way that you'd like to change it. Prompt the AI to make the change, and iterate until you get a version that you like.

Once you have your final filter, describe the aesthetic changes you wanted compared to the starting filter and how the code needed to change to get those results.


### DIY filter

Finally, make one more filter for an aesthetic of your choice. Put your code in a file named `diy_filter.py`.

Use AI to help you by suggesting the visual style you want, getting some code, then adjusting the paramters or iterating. Practice using rich, descriptive prompting language to clarify what you want. For example,

*Modify the program to create hazy, soft, lush nostalgic filter. Add soft blur, as if viewing a memory that's a little out of focus, and make the image slightly washed out and desaturated. The goal is to remove anything harsh or discordant from the image and create a relaxing effect in the viewer.*

(You can experiment with this one if you want, but make up your own example.)

Log the conversation that you have with the AI along with your assessment of each version of the filter.


## Submission

Upload the following files to the Project 1 assignment on Canvas:

- `warmup.doc`
- `filters.doc`
- `cool_filter.py`
- `vintage_filter.py`
- `diy_filter.py`

You **don't** need to submit the small programs you created in the warm-up section; your logbook is enough.
