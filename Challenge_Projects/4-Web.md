# Challenge Project: Front-End Web Development

## Due Monday, 4/25 (The last day of class)

## Description

This project has two parts. You need to complete both to get credit. Use an HTML/CSS/JS REPLit environment, like in our previous web programming examples.


## Smoot Converter

Oliver R. Smoot is an MIT graduate and former head of the American National Standards Institute (ANSI) and the International Organization for Standards (ISO).

In 1958, as part of his initiation into ΛXA, Smoot and his brothers measured the entire length of Harvard Bridge over the Charles River in Cambridge, MA, using Smoot’s body as the ruler. He was at the time 170 cm tall (5 feet, 7 inches), and the bridge was declared to be 364.4 Smoots, "plus or minus one ear" (about 2035 feet or 650.7 meters). Since that time, the measurement of Harvard Bridge has always been denominated in Smoots, with the markings repainted each year by the incoming ΛXA pledge class at MIT. The Cambridge police use the Smoot markings to identify the location of accidents on the bridge.

<img src="https://alum.mit.edu/sites/default/files/styles/article_desktop/public/images/SMOOT.jpg?itok=jMC7rC_T" width="35%" />

Create a web page that can be used to convert lengths from feet to Smoots and vice versa. Users should have a select box to choose which conversion they want (feet-to-Smoots or
Smoots-to-feet) with a box to accept input and a convert button. Output the conversion to two decimal places in a `<div>` and include the string `plus or minus one ear` in your
output.

Tips:

- Look up the `<select>` tag for examples of creating a select box. You can use the `value` property of your `<select>` item to get the selected option.

- Numbers have a `toFixed` method that will round to a given number of decimal places.


## Hipster Restaurant Menu Generator

*farm-to-table lamb crunchwrap $22*  
*eldritch sea scallop fettucine $18*  
*microwaved languostine globules $29*

I’ve decided to open a new restaurant and I need your help coming up with the menu. This place is going to be slick and hip, with all kinds of exposed ductwork, bricks, 
and those old-timey lightbulbs, so it needs a hip menu to match. In fact, I think the menu should be **randomly generated** using a context-free grammar.

<img src="https://travelgrrrls.files.wordpress.com/2019/05/edison-bar2.jpg" width="35%" />

[*LATFH*](https://travelgrrrls.wordpress.com/2019/05/02/hipster-light/)

In this project, you’re going to write a page that uses JavaScript and DOM-manipulation to automatically create a restaurant menu.

- Your menu is going to have three sections: appetizers, mains, and desserts. Each section should use a different set of ingredients and preparations and different generation 
rules so that the menu items are unique. Put at least three items in each section.

- Use `menu_generator.html` as a starting point. It shows an example of generating the appetizer section. Use the code as a template to finish the other two sections. You can 
modify the ingredients and options for the appetizers if you want to use my choices in other sections.

- Give your restaurant its own name and modify the hip styling so your page has its own look.
