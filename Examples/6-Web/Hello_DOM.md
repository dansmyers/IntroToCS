# Hello, DOM!

## Overview

This example will show you a page that demonstrates the essential techniques for working with the browser's Document Object Model (DOM). Recall that the DOM is like the
browser's in-memory representation of a page's contents. API calls can be used to interact with the DOM, which corresponds to making changes to the elements on a page.

We're going to talk about:

- Input boxes and buttons
- The DOM as a tree representation of a page
- Giving IDs to page elements
- Assigning a JS function to activate when the user clicks on a button
- Using `document.getElementById()` to get a reference to a DOM element
- Using the `innerHTML` property to change part of the page

## The Code

Copy this code into a file on Mimir, then run `srv` and view it. Interact with the page and verify that it does what it's supposed to do.

```
<!DOCTYPE html>
<html>

    <head>
        <title>Hello!</title>
    </head>
    
    <body>
        <h1>Hello!</h1>
        <p>Type your name and press the button.</p>    
        
        <!-- Declare a text input box -->
        <input type="text" id="text-input"/>
        
        <!-- Declare a button that runs the hello() function when it's clicked -->
        <!-- Note: you have to include the parentheses in "hello()" -->
        <button id="submit-button" onclick="hello()">Click Here</button>
        
        <!-- An initially empty div that will hold the response -->
        <!-- The hello() function uses DOM actions to put text here -->
        <div id="response-region"></div>
        
        <!-- JS code goes in the script tag -->
        <!-- Note that script is inside the body tag -->
        <script>
            function hello() {
                let textBox = document.getElementById("text-input");
                let name = textBox.value;
                
                let responseRegion = document.getElementById("response-region");
                responseRegion.innerHTML = "Hello, " + name + "!";
            }
        </script>
    
    </body>

</html>
```

The page is simple, but there's a lot going on here. Let's break it down.

- The third line of the body creates an input text box. The `<input>` tag can take many different `type` values, each one of which corresponds to a different
kind of input interaction. You can create, for example, radio buttons, checkboxes, password inputs, and date selectors just by changing `type`.

- The `input` tag has an `id` property, which assigns a unique name to this page element. **This is a key concept**: once we've assigned a name to an element,
we can interact it with it via JavaScript, which we'll discuss in more detail below. Note that you don't have to give an element an `id` if you don't need
to interact with it.

- The fourth line creates a button, which also has an `id` property. The button also has an `onclick` property, which specifies a JavaScript function to run
when the button is clicked. **This is the second key concept**: every time the user clicks the button, the browser will run the `hello()` function. There
are **many** different interactions that can be used to trigger JS functions; clicking is an obvious one, but you can also trigger events for things like mouse movement,
key presses, and even different phases of the page's loading lifecycle.

- The last element is a `div` that's empty when the page first loads. The `hello()` function will use DOM actions to put a string into the `div` when the user clicks the
button. **This is the third key concept**.

## What is the DOM?

The DOM is a **tree representation of all the elements on the page**. For our example page, a (slightly simplified) view of the DOM would be like this:

```
       html
        |
  -------------------
  |                 |
 head             body
  |                 |
 title              |
                    |
      --------------------------------
      |      |     |        |        |
      h1     p    input   button    div
```

The structure of the tree matches the structure of the page:

- `<html>`, the outermost tag, corresponds to the root of the tree.

- `<head>` and `<body>` are the direct children of `<html>`.

- The `<title>` tag, which is nested within `<head>` on the page, is its child in the DOM.

- The other page elements are all children of `<body>`; notice that those elements are siblings in the tree.

**Every element on the page corresponds to a DOM node, and nesting in HTML corresponds to hierarchy in the DOM tree**.

## Manipulating Elements

Recall, from above, that the `<button>` has its `onclick` property set to `hello()`. Whenever the user clicks the button, the browser will generate an event that
will run the code in the `hello()` JavaScript function.

The basic JavaScript function for interacting with page elements is `document.getElementById()`, which takes an element's `id` name as input and **returns a reference
to the element's DOM node**.

Here are the first two lines of `hello():

```
let textBox = document.getElementById("text-input");
let name = textBox.value;
```

The first line uses `document.getElementById()` to get a reference to the `text-input` box. The second line accesses the `value` property of the input box, which returns
the text it contains.

The second pair of lines makes a similar move: get a reference to the response `div` element, then set its `innerHTML` property to make text appear on the page:

```
let responseRegion = document.getElementById("response-region");
responseRegion.innerHTML = "Hello, " + name + "!";
```

There are **lots** of other manipulations you can do. In the project, you'll see an example of making new nodes and attaching them to the DOM, which has the effect of
making new content appear on the page.

## Review

Here is the basic strategy for creating interactive web pages.

- Set `id` names for the page elements the user needs to interact with or that you want to use as input.

- Set event properties, like `onclick`, to run JS functions when the user interacts with your page elements.

- In your JS functions, use `document.getElementById()` to get references to DOM nodes, then access or set their properties, like `innerHTML`, to make things happen on the page.

As you're practicing, you'll probably need to do some research to look up the events and element properties that you need to use for a particular effect. This is normal. Keep
playing around and experimenting!
