# Make a Graph

<img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Minard.png" width="100%" />

*Charles Joseph Minard's famous map showing the advance of Napoleon's army during the 1812 invasion of Russia and the subsequent retreat following the Battle of Moscow. The thickness of the line represents the size of the army. The bottom scale shows the temperature at key points during the retreat*.

*Napoleon entered Russia with an army of more than 650,000 men, the largest assembled in Europe up to that point. The survivors of the main invasion force numbered only 27,000*.

## Due Tuesday, 11/25 (right before Thanksgiving break)

## Overview

In this project, you will have the opportunity to conduct your own small scale research study, using a research question and data set that you select. The project has four parts:

1. Formulate a research question. More on this below.

2. Find a publically available data set that you can analyze to answer your question.

3. Use your data set to **make a graph in Python** that addresses your research question.

4. Make a **short** PowerPoint presentation, providing your question, details on your data set, the graph, and your interpretation of the answer to your question.

The goal of this project is to give you practice formulating a reearch question, conduct the research required to answer it, and then present your results in a technical write-up. This may serve as useful preparation if you are planning on doing a thesis project or taking other research-focused classes in the future.


## AI Use

**Use AI to help you**. Chat models are very good at working with Pandas and suggesting the appropriate functions to call to help you load your dataset and make the graph.

As before, keep a log of your interactions.


## Details

### Formulating Your Research Question

<img src="https://www.edwardtufte.com/tufte/graphics/vdqi_bookcover.gif" width="25%" />

There are lots of different approaches to research. Indeed, in some fields, you have to establish an entire **philosophy** of research before you can even begin to conduct a
study. In this project, we're going to focus on formulating a research question that can be answered using the visual presentation of quantitative information. That means you
want to formulate a question that can be answered, in one way or another, by looking at data plotted on a graph.

There is no specific area or topic that you're required to investigate, and your choice of question doesn't have to be related to any of your other classes or your major. In fact,
it's usually more interesting if you're exploring your own personal interests.

Let's talk about research questions. The most important rule of research questions is **to actually have one**. Many projects &ndash; particularly student thesis
projects &ndash; suffer because they begin with a vague general sense of direction, but not a concrete question for investigation (I have often been guilty of this in 
my own work). 

Research is not a mechanical process and studies can't proceed in a straight line, but it's almost always best to spend time at the start of your project developing and refining a core question that will motivate your study: it makes every aspect of the research process easier.

For this project, a good research question is **one that has a definite answer**.

- A yes/no question.
- A question about which of two things is larger or better by some measurement.

There are important research projects that focus on more open-ended investigations of systems, processes, or cultures, but they're beyond the scope of what we're trying to do here.

Think about formulating a question with the following qualities:

- It's a question, not a statement.
- It has a relatively small set of potential answers.
- You don't know the answer in advance; any of the possible answers could be reasonable.
- Questions that start with *Which*, *What*, *Who*, *How many*, or similar phrases are often good. Questions that start with *How*, or *Why* are more like process questions, and require different set of investigative techniques.

### Find the Data Set

Once you have a research question, you need to find a publically available data set that will allow you to answer it. Here's the only guideline for this step:: **Your data set must be publically available on the Internet or in a publication**. **Don't collect your own data**.

There are lots of potential sources:

- There are many repositories of public data sets on the Internet.
- Sports statistics are readily available.
- The Kaggle site has lots of interesting data sets used for analytics and machine learning competitions.
- Metacritic and other sites that aggregate review information.
- Box office data or book publishing numbers are also available through Wikipedia or other sites.
- Many companies publish internal data in blog posts.
- You could consult with a librarian to help you!

**Your data set is not required to be from a peer-reviewed source**, so you are able to work with information from a wider range of domains without needing to conduct an extensive literature search. Please do consider whether your source is reasonable and likely to be reliable as part of the selection process. There's no minimum required size.


### Make the Graph

Once you have your data, you'll probably want to put it into a CSV file and load it into Pandas. From there, you can make whatever kind of graph is appropriate to help answer your question. **You have to use Python and Pandas for this project**.

Remember some key rules of good graphing:

- Choose the appropriate graph style. For example, don't use a line plot for discrete data: a bar chart or scatter plot usually makes more sense.
- Label your axes and include units.
- Begin the vertical axis at zero unless you have a very good reason not to.
- Use colors or line styles to distinguish between categories, if necessary.


### Slides

Once you have your graph, make a four-slide presentation, as follows.

- Slide 1: Question
  - State the research question
  - Explain, in a few points, why it is interesting
 
- Slide 2: Data
  - Summarize the data set you are using
  - Where is it from? What does it contain?
  - Give a citation for the source

- Slide 3: **The Graph**
  - Only the graph, nothing else
  - The graph fills the entire slide
  - It stands on its own and in a talk you would spend a good chunk of time explaining its structure and interpreting it
  - Remember that the graph needs a title, labeled axes with units, and a legend if necessary
 
- Slide 4: Summary
  - State the answer to your question
  - Explain, in a few points, how the graph allows you to make that conclusion
 
Pro-tip: **Never** end on a slide that just says "Questions?" It's the end of your presentation! It's understood that there will be an opportunity to ask questions! Always end on a slide that restates the main points of your presentation, so the audience will see them and use them as the basis for any discussion.


## Submission

Submit the following:

- The script that loads your dataset, analyzes it, and makes the graph
- Your four-slide PowerPoint deck
- Your AI log

You don't need to submit the dataset itself.
