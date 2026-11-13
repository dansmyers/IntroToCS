# My Heart Will Go On

<img src="https://i.ytimg.com/vi/kEPfM3jSoBw/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLASDLwZJ2zstmie_gzbcUGl5-jXmQ" width="400px" />

*[Titanic with a Cat](https://www.youtube.com/watch?v=kEPfM3jSoBw) by OwlKitty*


## Overview

Let's get started with the "Hello, World" of data analysis the *Titanic* data set.

The goal of this activity is to help you practice writing and running programs through the standard chat interface. It will also demonstrate some useful techniques and standard tools for data analysis in Python.

After completing this activity, you'll be familiar with:

- CSV files
- Python's Pandas and matplotlib libraries
- The concept of a Pandas dataframe
- Using chat to analyze a data set and produce a plot
- Making edits to a program using chat

## The *Titanic* Dataset

<img src="http://4.bp.blogspot.com/-B_jEnnLjgI0/U-_r3-pZr6I/AAAAAAAA3lM/UzMzMqlDSsQ/s1600/1977114_10152475439781112_174145227163964287_n.jpg" width="300px" />

In the early hours of April 15, 1912, the "unsinkable" ship *RMS Titanic* sank when it struck an iceberg, killing more than half of the passengers and crew aboard. The `Titanic.csv` dataset contains demographic information for 889 of those passengers as well as a record of whether or not each passenger survived. Our first goal is to explore the functionality of Pandas by opening and modifying the *Titanic* dataset.

I sent you a copy of the file by e-mail, or you can find it in this repository. If you open the file, you'll see the following lines at its top:
```
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare
0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25
1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833
1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925
1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1
0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05
0,3,"Moran, Mr. James",male,,0,0,330877,8.4583
```
The data is stored in **comma-seperated value** format, a standard way of representing spreadsheet data as plain text. Each line of the file corresponds to the entry for one passenger, like a row in a spreadsheet. The different fields for each passenger are separated by commas.

The data set has eight fields. Notice that their names are given on the first line of the file, which is standard for the CSV format.

- `Survived`: a 0/1 value indicating whether the passenger survived
- `Pclass`: 1, 2, or 3 indicating whether the passenger was in first, second, or third class
- `Name`
- `Sex`: The string `male` or `female`
- `Age`
- `Siblings/Spouses_Aboard`
- `Parents/Children_Aboard`
- `Fare`: The amount, in 1912 British pounds, paid by the passenger

For example, the second passenger is:
```
1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833
```
This tells us that Mrs. John Bradley (Florence Briggs Thayer) was a 38 year-old woman who sailed in first class. She survived the sinking. She paid a fare of £71.2833, in *1912 British pounds*, which is about £10,500 today.

## Plot

Claude can write programs, run them, and produce outputs within the chat window. In general, using that chat is a fine choice for small programs that you only need to run once and that will produce a well-defined output. Simple data analyses are a good example.

Chat is *not* a good choice for programs that you need to save and run multiple times, or for interactive programs.

Upload a copy of the Titanic.csv file into your chat window. You can do this by dragging and dropping the file from your Downloads folder, or by using the `+` button in the chat window to add the file.

Then prompt Claude:
```
Create a Python script that analyzes the attached Titanic.csv file and outputs a bar chart showing the survival rates of passengers in each of the three classes. Use Pandas for data analysis and matplotlib for the plot. Ask me if you have questions before writing any code.
```

**Tip**: I always like to prompt the model to ask clarifying questions. As we'll see in future activites, Claude is very good at helping you explore the design of a program.

Run the prompt. It will crank for a few seconds and then produce the graph and code as artifacts that you can examine. Take a look at both.

## Tools

**Pandas** is the standard Python library for data analysis. A typical Pandas program starts by loading the data from your CSV file into a *dataframe*, which is Pandas' main way of representing spreadsheet-style data in code. If you look at your program, you'll see a line like the following near the top:
```
df = pd.read_csv('/mnt/user-data/uploads/Titanic.csv')
```
This line uses a built-in CSV reading method to load your file into the computer's memory. The result is a dataframe that is named `df`. You can think of `df` as a table, where the rows are passengers and the columns are the fields, like the following:
```
Survived  Pclass                                               Name     Sex   Age  Siblings/Spouses_Aboard  Parents/Children_Aboard     Fare
       0       3                             Mr. Owen Harris Braund    male  22.0                        1                        0   7.2500
       1       1  Mrs. John Bradley (Florence Briggs Thayer) Cum...  female  38.0                        1                        0  71.2833
       1       3                              Miss. Laina Heikkinen  female  26.0                        0                        0   7.9250
       1       1        Mrs. Jacques Heath (Lily May Peel) Futrelle  female  35.0                        1                        0  53.1000
       0       3                            Mr. William Henry Allen    male  35.0                        0                        0   8.0500
```

Pandas provides the ability to do a wide variety of manipulations and calculations on dataframe objects.

The second library we're using is matplotlib, which is a standard plotting library. If you look at your program, you'll see lines that do things like create a new figure, plot a bar chart onto it, then assign things like axis labels, a title, etc. Python can produce almost any kind of plot, but the syntax for the commands is often tedious, which is where AI is a big help.

## Practice

1. Take a look at the plot. Identify one thing about it that you'd like to change, then prompt Claude to update and re-run your code.

2. Identify one line in your script that seems complex. Ask for an explanation of what it's doing. Claude is good at explaining code.

3. Prompt Claude to modify the plot to produce the survival rates separated by both passenger class and sex. As before, take a look at the plot and ask it to make changes to get the style that you want.

## Conclusion

This small example illustrates an important point: **A large part of programming is stitching together useful features from tools and libraries that already exist**. We don't have to write all of the low-level data loading and manipulation code, because Pandas is a readily-available framework that will do it for us.

AI is *very good* at writing this type of compositional code. Part of the design process is identifying frameworks that you can leverage to reduce the complexity of your program.
