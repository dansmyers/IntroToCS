# Intro to Web Pages

<img src="https://static0.polygonimages.com/wordpress/wp-content/uploads/chorus/uploads/chorus_asset/file/22421821/NbKPigG.png" width="400px" />

The original website for *Space Jam* from 1996 still exists. You may not like it, [but this is what peak performance looks like](https://www.spacejam.com/1996/).

## Overview

This short lab will let you practice jamming on simple HTML and CSS, two of the core technologies of front-end web programming. By the end of it, you should feel comfortable with the idea of representing web page content using tagged text and simple styling.

## Setup

Create a `Lab_14` directory and `cd` into it.

## Write and serve a basic web page

### Creating the page

Let's make a basic web page. Put the following text in `index.html`. I'll tell you more about how this file is put together in the next section, after you've had the
chance to run and display it.

```
<!DOCTYPE html>
<html>
    <!-- This is an HTML comment -->
    <!-- 
        The basic HTML file has two sections:
        <head> contains metainformation on the whole page
        <body> contains page content
      -->

    <head>
        <title>This appears at the top of the browser.</title>
    </head>
    <body>
        <h1>This is a Website.</h1>
        
        <p>This is a paragraph of text on a website.</p>
        
        <p>Here's another paragraph.</p>
        
        <p>That's all.</p>
    </body>
</html>
```

### Serving

Web pages are fetched and displayed by a browser using the *Hypertext Transfer Protocol* (HTTP). A web server is a program that can receive HTTP requests and return requested pages.

Python has a simple built-in web server that you can use to view your page. Type the following command in the terminal:
```
python -m http.server 8080
```
This should create a pop-up in your window asking if you want to open the page on port 8080. Choose yes and you should see a browser tab pop up with the text of the demo page.

**What's up with that special 8080 number?** Every program that makes network connections is assigned a unique *port number* that the operating system uses to route incoming network requests to the appropriate destination. You can think of the port number as being like a mailbox number for a particular program running on a specific computer. In this case, the OS understands that incoming requests labeled with port 8080 as their destination should be routed to the Python web server program for processing. 

The port number could be any integer from 0 to 65535, but most common web applications have standardized port numbers. It's traditional for web servers to run on ports 80 and 8080.

**Stop the server**. After you've viewed the page, use CTRL + c in the terminal to stop the server.


### Page contents

Web pages are written in **HTML**, the *Hypertext Markup Language*. An HTML file is a mixture of regular text and special **tags** that tell your web browser how to format the page.

All tags are enclosed in angle brackets.

The top-level tag is `<html>`, which encloses all of the page content. Inside the `<html>` tag are two main sections:

- `<head>`, which is used to hold meta-information about the page.
- `<body`>, which stores the actual page content.

Notice that all of the tags have an opening version, like `<body>`, and a closing version with a slash, like `</body>`

Your example page uses two other tags

- `<h1>` is the top-level header tag. Anything you put between `<h1>` and its closing partner `</h1>` appears big and bold when the page renders. There are also `<h2>`, `<h3>`, and `<h4>` tags.

- `<p>` is the paragraph tag, to make a new section of text on the page.

### Jam

Before going further, experiment with making some changes to your page and visualizing the results. Re-run the serber using the command above, reload the page, then stop the server using CTRL + c when you need to make changes.

**Put all of your page content into the current `<body>` tag**. The browser will try to make sense of anything you give it, but a page should have *one* `head` block and *one* `body` block enclosed in the `html` tags. Don't paste additional content below the current `</html>` tag.


Try creating an unordered list of items using the `<ul>` and `<li>` tags:
```
<p>Ian's stuffed animals:</p>

<ul>
    <li> Pickles the tiger
    <li> Manny the Manatee
    <li> Douglas the brown owl
</ul>
```

You can create a link using the `<a>` tag (for "anchor"). The tag contains a parameter called `href` that specifies the destination of the link:
```
<a href="https://squishmallows.com">Will loves these and calls them "Blobbers".</a>
```

### Interior decoration

Let's add an image to the page. The easiest way to add an image is to directly to it from your page. Add the following tag within the `<body>` region:
```
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg"/>
```
The `src` parameter supplies the URL of the image. Notice that the URL has to be enclosed in parentheses. Reload the page and check out your picture.

Yikes. That's large. You can add style to the tag to scale the image to a percentage of the display width:
```
<p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg" style="width:50%"/>
</p>
```
You can also set an absolute size in pixels, e.g. `"width:200px"`.

You can also serve images directly out of your project directory. The easiest way to do this is to first download them to your computer, then upload them back to the Codespaces directory. For example, if you had downloaded and the uploaded an image called `cheezburger.jpg`, you could add it your page using
```
<img src="cheezburger.jpg" />
```
Find another image and add it to your page with a second `<img>` tag.


### Alt text

What happens if you try to load an image that doesn't exist?
```
<img src="DOES_NOT_EXIST" />
```
You will see a broken image placeholder appear on the page. For accessiblity reasons, it's useful to include **alt text** for your images. The `alt` field specifies descriptive text that the browser can display if it can't load the image. These fields are used by screen readers to supply descriptions of the page.

```
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg" style="width:50%", alt="Image of The Great Wave off Kanagawa by Katsushika Hokusai"/>
```


## A little CSS

Styling elements using individual tags was common in the old-school web, but modern practice favors separating page content from styling. Let's add a `<style>` section to the `<head>` block that will hold rules for styling page elements. The language used for styling web pages is called **CSS**, which originally stood for *Cascading Style Sheets*, but that name is mostly a historical artifact at this point.

- HTML controls the page's content and overall structure
- CSS controls its style and formatting

```
<head>
    <title>This appears at the top of the browser.</title>

    <style>
        img {
            width: 50%;
        }
    </style>
</head>
```

The style rule specifies that the contents of all `<img>` tags should have their width set to 50% of the page size. Remove the `width:` attribute from the `img` tag in the body of the page, then reload the page and verify that the CSS rule causes the image to be displayed at 50% width.

### More style rules

You can add elements to the style block to control the presentation of other parts of the page. For example, to style the contents of  the entire body:

```
<head>
    <title>This appears at the top of the browser.</title>

    <style>
        img {
            width: 50%;
        }

        body {
            font-family: "Helvetica", "Arial", sans-serif;
            font-size: 18pt;
            background-color: #FAFAFA;
        }
    </style>
</head>
```

**Fonts** The `font-family` parameter takes a list of fonts (a "font stack") and uses the first one that's available on the system. Here, the first choice font is Helvetica and the last choice is the default system sans-serif font, which is guaranteed to exist in every browser. `font-size` controls the size.

**Colors** Colors are specified as three values, denoting the red, green, and blue components of the color. Each value is represented using the **hexadecimal** number system, which encodes a byte of data as a number from `00` to `FF`.

The string `#FAFAFA` sets R, G, and B to a nice equal gray color, slightly off-white. For something more vibrant try

- `#0071BA` (the official brand-approved Rollins blue color). This color has no red (`00`), some green (`71`) and a good amount of blue (`BA`).
- `#FACF00` (the official brand-approved Rollins gold color). This color has a lot of red (`FA`), a good amount of green (`CF`), and no blue (`00`).

Play around with a color picker and experiment with different color strings:

https://htmlcolorcodes.com/color-picker/

You can also set the `color` property to control the color of the text.


### a e s t h e t i c s

Here's one last style block that makes things a little more readable by bringing the page contents to the center.

```
<style>
    img {
        width: 100%;
    }

    body {
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 18pt;
        color: #333333;
        background-color: #FCFCFC;
        margin: 40px auto;
        max-width: 640px;
    }
</style>
```

`max-width` controls the size of the display region in the browser.

`margin` sets a padding of 40px around all sides of the page content; `auto` centers the display region inside the browser frame, pulling everything to the middle. Note that this is centering the display region, not the content itself.

The background and text are softened a little away from strict white and black.

# Interactive Pages

The second part of the lab will demonstrate how to add *interactivity* to a page.

It's common to have applications accessed through a browser. The web page becomes the graphical front-end of the program and the user interacts with page elements to do things. Some actions may trigger requests that go to the application's back-end server to fetch more data. Think about a social media feed, for example. As you scroll, the application is updating with more related content and maybe placing ads into your feed that it generates based on its profile of your use.

**JavaScript** is the language used to program interactive web pages. JS code is embedded into pages, which can then be interpreted by an engine that's built into your web browser. JS makes it possible to write functions that trigger as the user interacts with page elements.

## Button

Here's a simple page with a new element: a button.
```
<!DOCTYPE html>
<html>

    <head>
        <title>An interactive page with a button</title>
    </head>
    <body>
        <h1>Click the button.</h1>
        
        <!--Create a button element-->
        <button>This is the button</button>

        <!-- The script block contains JavaScript code -->
        <script>
            // Empty for now: we'll fill this in later
        </script>
    </body>
</html>
```

Put the code into a new file named `button.html`. When you run the server, click on the URL bar at the top of your browser to append `/button.html` to go to the new page. For example, if your starting URL was
```
https://probable-xylophone-x5qq9496j64fpvw6-8080.app.github.dev
```
You would go to the address:
```
https://probable-xylophone-x5qq9496j64fpvw6-8080.app.github.dev/button.html
```

## Alert
Experiment with clicking on the button. You'll see that it doesn't do anything. Elements like buttons don't have any default behavior. Instead, we have to connect the button to a function, then write code that performs the action we want the button to trigger.

First, update the `<button>` tag to the following:
```
<button onclick="hello()">This is the button</button>
```
The structure is important:

- The `onclick` statement is inside the angle bracket with `button`
- `"hello()"` must be enclosed in quotes and have the parentheses

`onclick` is a built-in property that the browse allows you to add to page elements. If `onclick` is set, then the browser will trigger the specified JS function whenever you click on the element. In this case, clicking on the button calls a JS function named `hello`, which we need to add to the `<script>` block.

Update the script block to the following:
```
<script>
    // Pop up an alert box that says 'Hello!'
    function hello() {
        alert('Hello!');
    }
</script>
```
Reload the page, then click on the button. You should see a box pop up with the message inside it. Each time you click will produce an alert.

JS code looks different than Python, but you should be able to follow what's going on:

- Comments are denoted with slashes, `//`
- The `function` keyword declares a new function, like `def` in Python
- Blocks of code are delimited by curly braces, like in Java and C
- Each line of code ends with a semicolon

### Experiment
Try modifying the message to say some different things. Then add a second button to the page with its own function.

## A more complex page

Here's a final example, which extends the basic button clicking idea to read from a text box and produce an output message.
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
        <button onclick="hello()">Click Here</button>
        
        <!-- The hello() function will put text inside this div region -->
        <div id="response-region"></div>
        
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

Here's a summary of the page elements:

- The third line of the body creates an input text box. The `<input>` tag can take many different `type` values, each one of which corresponds to a different
kind of input interaction. You can create, for example, radio buttons, checkboxes, password inputs, and date selectors just by changing `type`.

- The `input` tag has an `id` property, which assigns a unique name to this page element. **This is a key concept**: once we've assigned a name to an element,
we can interact it with it via JavaScript. Note that you don't have to give an element an `id` if you don't need
to interact with it.

- The fourth line creates a button. The button has an `onclick` property that runs the `hello` function when it's clicked.

- The last element is a `div` that's empty when the page first loads. The `div` tag is short for "division" and is used to mark out a region of the page for some specific purpose. The `hello()` function will use DOM actions to put a string into the `div` when the user clicks the
button. Notice that the `div` element has its `id` property set to `response-region`.

### The Document-Object Model (DOM)

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


### Manipulating Elements

Recall, from above, that the `<button>` has its `onclick` property set to `hello()`. Whenever the user clicks the button, the browser will generate an event that
will run the code in the `hello()` JavaScript function.

The basic JavaScript function for interacting with page elements is `document.getElementById()`, which takes an element's `id` name as input and **returns a reference
to the element's DOM node**. Here are the first two lines of `hello():
```
let textBox = document.getElementById("text-input");
let name = textBox.value;
```
The first line uses `document.getElementById()` to get a reference to the `text-input` box. The second line accesses the `value` property of the input box, which returns
the text it contains. The `let` keyword is used to declare variables in JavaScript.

The second pair of lines makes a similar move: get a reference to the response `div` element, then set its `innerHTML` property to make text appear on the page:

```
let responseRegion = document.getElementById("response-region");
responseRegion.innerHTML = "Hello, " + name + "!";
```

### Experiment

Modify the code to make the output print something else.

# Questions

Do a little research and answer the following questions:

- What's the difference between the Internet and the Web?
- What is meant by the term *hypertext*?
- Who is the creator of the World-Wide Web (WWW) and when and where was it created?
- What was the motivation for creating the WWW?
- What are URLs?
- Find the oldest existing web page.
