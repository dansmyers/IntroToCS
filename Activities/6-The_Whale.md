# Zipf's Law and *The Whale*

<img src="http://www.harkavagrant.com/history/moby.png" width="300px" />

Kate Beaton, *Hark! A Vagrant* [66](http://www.harkavagrant.com/index.php?id=66)

## Overview

Zipf’s Law is a result from linguistics that describes the distribution of word frequencies in many texts. It states that the Nth most frequent word occurs about 1/N times as often as the most frequent. That is, the second most frequent word occurs about 1/2 as often as the most frequent word, the third most frequent about 1/3 as often, and so forth. The law is named for George Zipf, who first described it based on empirical observations in the 1930s.

Let’s vibe out a program that can analyze a text — we're going to use *Moby Dick*, of course — and make a plot demonstrating if it follows Zipf’s Law. 

## Text

A copy of `moby_dick.txt` is posted to Canvas. Download it to your computer and then you can upload it to your Claude chat.

## Start by chatting

We might be able to get a usable solution by just asking directly for “a program that can analyze a text and see if obeys Zipf’s Law”, or something similar. It’s a better idea, though, to start by having a conversation about the requirements, which will give you an opportunity to clarify what the program needs to do.

Go to Claude and try the following prompt:

> I would like to write a Python program that can count the frequencies of words in moby_dick.txt and plot them to examine if the text obeys Zipf's Law. I want the output to be a plot saved as a PNG file. Act as my co-programmer and discuss this program with me. Help the clarify requirements and understand the overall design. Assume that I have very little programming experience. Don't generate any code yourself yet, just help me create a plan for this project.

Don’t worry about making the best possible prompt! Modern models don’t need tricky prompt engineering. Instead, just start with your work in progress and have a conversation about what to do next.

Claude comes back with a few clarifying questions, which might be similar to the following:

>- How should we handle punctuation and capitalization? (e.g., should "The" and "the" be counted as the same word?)
>- Should we exclude common words like "the", "and", "of"? (called "stop words")
>- What scale should we use for the plot? (Zipf's Law often shows up best on a log-log plot)

This is exactly what we wanted! AIs are generally good at providing this sort of clarifying feedback. **Always start your program by having a chat about the goals and requirements before you jump into generating code**. If you have questions about your options, just ask for more information and help deciding.

I went back in and answered Claude’s questions:

> I would like to produce a plot showing the word frequency data and comparing it what would be expected by Zipf's Law. We should ignore capitalization and punctuation and treat all occurrences of the same word as identical.

Your output to the first step, and hence your response, might be slightly different from mine, but notice that we’re just having a conversation about what we want the code to do.


## Generate

Now ask Claude to generate the code. This should take a few seconds. You can then prompt it to run the program.

When you run, Claude will pop up a permission box asking if it's allowed to run the program using `python`. You can choose to allow the action one time (which will cause Claude to re-ask for future permissions) or allow all 

## Check the output

Your program should run and produce a PNG file as its output. Take a look at the image and see if it makes sense. Make sure that the output obeys some qualities of good graphing:

- Title
- Axis labels
- Lines distinguished by style with a legend to explain which line is which. Use line style (e.g., solid vs. dotted vs. dashed) when you have a small number of curves to distinguish rather than colors.

If you need to make any edits to the figure, prompt Claude to update the code, then re-copy and re-run the updated version until you get a good looking plot.

## Variations

Try prompting in a few changes to the code:

- Add an annotation on the plot to show where the word “whale” appears in the data
- Remove the most common English words (the, and, a, of, etc.) that tend to dominate the top of the distribution and re-run the analysis
