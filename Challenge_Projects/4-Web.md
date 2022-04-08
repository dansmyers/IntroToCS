# Challenge Project: Front-End Web Development

## Due Monday, 4/25 (The last day of class)

## Description

This project has two parts. You need to complete both to get credit. Use an HTML/CSS/JS REPLit environment, like in our previous web programming examples.

## DOM

<img src="https://images.saucey.com/large/dom-perignon.jpg" width="35%" />

Start by taking a look at the `Hello_DOM` file in the `Examples` directory to review the techniques we talked about in class. Those notes introduce a new term: the *Document Object Model* (DOM), which is the browser's in-memory representation of all the elements on the page. When you interact with page elements in JavaScript code (for example, by reading a `value` property or setting `innerHTML`), you're really interacting with the browser's underlying DOM representation of those elements.

The (MDN tutorial)[https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction] summarizes it like this:

> The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.



## Smoot Converter

Recall the story of Oliver R. Smoot, MIT graduate and former head of the American National Standards Institute (ANSI) and the International Organization for Standards (ISO).

In 1958, as part of his initiation into ΛXA, Smoot and his brothers measured the entire length of Harvard Bridge over the Charles River in Cambridge, MA, using Smoot’s body as the ruler. He was at the time 170 cm tall (5 feet, 7 inches), and the bridge was declared to be 364.4 Smoots, "plus or minus one ear" (about 2035 feet or 650.7 meters). Since that time, the measurement of Harvard Bridge has always been denominated in Smoots, with the markings repainted each year by the incoming ΛXA pledge class at MIT. The Cambridge police use the Smoot markings to identify the location of accidents on the bridge.

<img src="https://alum.mit.edu/sites/default/files/styles/article_desktop/public/images/SMOOT.jpg?itok=jMC7rC_T" width="35%" />

Create a web page that can be used to convert lengths from feet to Smoots and vice versa. Users should have a select box to choose which conversion they want (feet-to-Smoots or
Smoots-to-feet) with a box to accept input and a convert button. Output the conversion to two decimal places in a `<div>`.

Tips:

- This is going to be very similar to our basic web programming example: there's an input box, a button that runs some JS code, and an output `<div>`. The one new element is the `<select>` tag.

- Give each element on your page an `id` label so you can interact with it.

- I recommend that you start by writing a version of the page that doesn't use `<select>` and just converts from feet to Smoots. You can then add `<select>` to choose between the two options.

- Develop incrementally! For example, start by just tying your button to a JS function that runs and produces an alert box. After you can do that, read the input value from the text box and alert the result. Then move the result to the output `<div>` element.

- Use alert statements to check your intermediate output. You can also print to the console using the `console.log()` function.

- Look up the `<select>` tag for examples of creating a select box. Like with a text box, you can use `document.getElementById` and the `value` property of your `<select>` item to get the selected option.

- JavaScript Numbers have a `toFixed` method that will round to a given number of decimal places. Do a search to learn how to use JS's `toFixed`.


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

- Use `menu_generator.html` as a starting point. It shows an example of generating the appetizer section. Use the code as a template to finish the other two sections. You can  modify the ingredients and options for the appetizers if you want to use my choices in other sections.

- You don't have to write that much code for this problem. Part of the challenge here is looking at the program and understanding how all of it fits together.

- Give your restaurant its own name and modify the hip styling so your page has its own look.

## Submission

Upload two HTML files, one for each problem, through Canvas. I recommend creating a different REPLit workspace for each problem, then putting all of your HTML and JS in a single `index.html` file for that problem.
