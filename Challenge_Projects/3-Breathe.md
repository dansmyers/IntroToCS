# Breathe

<img src="http://portlandartmuseum.us/MWEBimages/IMAGES/PERMANENT%20COLLECTION/2024/2024_0031_0006i_20250421_P.jpg" width="320px" />

*Landscape - Sagittarius, from the series Zodiac*, Yoshida Hodaka (1973). Via the [Portland Art Museum](http://portlandartmuseum.us/mwebcgi/mweb.exe?request=record;id=87633;type=101).


## Tuesday, 5/5 (the last day of finals)

## Overview

Let's practice using the specs-driven development approach we discussed in class to make a web-based breathwork app.

- The app will run as a single front-end web page using HTML, CSS, and JavaScript. Take a look at Challenge Project 2 if you haven't done so yet.
- It will have some controls to allow the user to select a breathing pattern and a visual and timer to help count each step

I've written the instructions below to use Claude, but you can use any of the major AI models that you want.

## Build the spec

The first step is to chat about the project with Claude to build a specifications document. Go to the regular Claude chat - I find it better for this step than using the terminal app. Prompt:
> I want to create a breathwork app. It should run as a single front-end web page. I want to be able to select a breathing pattern and have a visual and a counter that helps with the counting of each step. Please chat with me and help me produce a specification in Markdown format for this project that I can give to me AI coding agent. You don't need to write any code, just help me produce the spec.

After this, Claude will ask you some questions. Chat about them. The key to this step is **having opinions and ideas** that can drive the specification. If you don't understand a questions, ask Claude to explain it to you. This is a great learning tool.

After you've worked through the discussion, ask Claude to output a spec document in Markdown format. Markdown is a way of representing structured documents in plain text. It's a preferred way of giving information to models because it's easy for them to understand, compared to more complex formats like PDFs and Word docs.

## Read the spec

Take a moment to actually read through the spec document. Double-check the choices it contains. If you have any questions, you can ask about them (again, this is a great way to learn about design). If you find something you want to change, just ask Claude to update the document.


## Build

Once you're satisied with the spec, ask Claude to use it to implement the program as a single front-end web page. It should build one for you in a few seconds.

Create a directory on your Codespace for this project, `cd` into it, then copy the code from your chat into a file named `index.html`. Run the web server by typing
```
python -m http.server 8080
```
at the terminal. Python will start the server and then you'll be prompted to open up a tab to view the page.


## Test and iterate

Identify a few changes you want to make. Even if you like the app as it is, think of something that could be changed. Then, **update the spec** to describe the change you want. This is important - the spec is the ground truth for the app, so you want to always make sure changes are reflected in it. If the project gets out of synch with the spec, the model has no reference to use to guide its code generation.

You can do the update by prompting Claude to change the spec, or by editing it yourself.

Then, prompt Claude to rebuild the app using the updated specification document. This step illustrates a key idea for working with agents: **code is cheap**. The overhead of generating something multiple times is low, so it's often more efficient to update the spec and rebuild the project, rather than trying to make changes to the already-existing code.
