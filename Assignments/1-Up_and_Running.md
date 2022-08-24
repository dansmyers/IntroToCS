# Assignment 1

## Overview

## Problems

### Our Princess is in Another Castle

<img src="https://cdn.mobilesyrup.com/wp-content/uploads/2020/11/super-nintendo-world-scaled.jpg" width="50%" />

*Super Nintendo World Japan. Coming to Universal Orlando in a few years.*

At the end of each level of the original Super Mario Bros., Mario jumps up a staircase like the following:

```
     ##
    ###
   ####
  #####
 ######
#######
```

The staircase has six levels. The bottom level has seven blocks and the top level has five spaces and two blocks.
Write a program that uses six print statements to print this staircase.

### Haiku

<img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Kobayashi_Issa-Portrait.jpg" width="25%" />

Write a program to print the following haiku by the poet Kobayashi Issa, famous for his works focusing on insects and other small creatures.

```
O snail
Climb Mount Fuji,
But slowly, slowly!
```

Use three print statements, one for each line.

Tips:

- Your output must match the format of the poem exactly to pass the test.
- Remember to start the program with a docstring.


### Beards

The beard-second is an incredibly scientific unit of length defined as the distance an average beard grows in 1 second. Google defines the beard-second as 5 nanometers and will perform conversions between beard-seconds and other lengths (try typing “1 foot in beard-seconds” into Google). Using this definition, it would take an average beard 58.8 days to grow 1 inch.


The longest beard in the world is 17 feet long and is housed in the Smithsonian institution. In life, it belonged to Hans Langseth, who immigrated to the U.S. from Norway in 1864; he died in North Dakota in 1927. He would wrap his beard around a corncob and carry it in his pocket.

<img src="https://upload.wikimedia.org/wikipedia/commons/8/81/Hans_Langseth.jpg" width="25%" />

Under the (completely unrealistic) assumption that Hans Langseth grew his entire beard at the average rate of 1 inch every 58.8 days, how many days would it have taken to him to get 17 feet of facial hair? Write a Python program that **calculates and prints** the answer.


### 1 Barnum = 1 Sucker / Minute

P.T. Barnum was a 19th Century showman, promoter, and politician, founder of the Barnum and Bailey Circus. He’s credited with coining the saying, “There’s a sucker born every minute,” although there’s no evidence he actually said this.


Jonathan the tortoise is the oldest known living terrestrial animal. He was hatched in the Seychelles, then transported to the island of Saint Helena in the South Atlantic Ocean in 1882, where he still resides. Measurements show that he was at least 50 years old when he arrived on Saint Helena, so he must have hatched no later than 1832, giving him an estimated age of 190 years old.


<img src="https://petapixel.com/assets/uploads/2022/01/jonathan-the-190-year-old-tortoise-with-1886-photo.jpg" width="40%" />


If Barnum’s alleged saying is true, how many suckers have been born during Jonathan’s life? Let’s assume that Jonathan is exactly 190 years old and that each year has 365 days (ignoring leap years). Write a Python program that calculates and prints the answer

### That's So Raven

<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Paul_Gustave_Dore_Raven14.jpg" width="25%" />

*Illustration by Gustave Doré (1884)*

Python quotes can be delimited using either double quotes, `" "`, or single quotes, `' '`. What if you want to put a literal quote inside a string? There are two ways.

First, you can use single quotes to mark the outside of the string, and use double quotes inside it, or vice-versa, depending on what kind of quote you need. For example,

```
print('Quoth the Raven "Nevermore"')
```

A second approach is to use a special character sequence, `\"`. When Python encounters the `\"` sequence in a string, it will replace it with the regular double quote, `"`.

Think of the `\` as being an "escape" character: it indicates that the following quote character should be treated differently from a regular double quote used to mark the end of a string. For example, the print statement

```
print("Quoth the Raven \"Nevermore.\"");
```

will print

```
Quoth the Raven "Nevermore."
```

Use five print statements and `\"` characters to print the *The Raven* as a limerick:

```
There once was a girl named Lenore
And a bird, and a bust, and a door
And a guy with depression
And a whole lot of questions
And the bird always says "Nevermore"
```

### More Smoots

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Burj_Khalifa.jpg/800px-Burj_Khalifa.jpg" width="25%" />

Recall the story of Oliver R. Smoot. The Harvard Bridge (2035 feet in length) was measured to be 364.4 Smoots, "plus or minus one ear". One Smoot is about 5.5833 feet.

The Burj Khalifa in Dubai is the tallest tower in the world, measuring 2722 feet to its top spire. What is the height of the Burj Khalifa in Smoots? Add the string "plus or minus one ear" to your output, so that it looks like this:

```
X plus or minus one ear
```

where `X` is the calculated answer value.

Tip: If you want to put a calculation into a print statement, you have to turn it in to a string using the str function. For example, the Harvard Bridge calculation could look like the following:

```
print(str(2035 / 5.5833) + ' plus or minus one ear')
```
