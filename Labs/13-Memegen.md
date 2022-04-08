# I CAN HAZ MEMEZ?

## Overview

In this lab, you're going to build a meme generator using front-end web development techniques.

The goal of this lab is **not** to memorize every single feature and function that's used to build the app. Rather, we want to emphasize
a few key points:

- The core technique of giving elements `id` values and accessing their properties using `document.getElementById()`.

- Laying out a page using Bootstrap's grid system.

- Using Bootstrap's built-in features for input boxes, buttons, and radio toggles.

- Assigning functions to run on button clicks and other events.

- Using a new element, `canvas`, for drawing.

Everything you'll create today will be **pure front-end HTML, CSS, and JavaScript**. All of the code fits into about 100 lines on a single
page. Therefore, the page can respond to user input, but doesn't have the ability to save data between session. Our next topic will be
adding in a back-end framework that can store and retrieve data in response to browser requests.

The lab should take about an hour. Once you finish you can make some memes and experiment with adding new features to the application.

## Initialization


Open `index.html` and you're ready to start coding. Here's a shell Bootstrap page. Copy and paste it into your `index.html`.

```
<!doctype html>
<html>
    
    <head>
        
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        
    </head>
   
    <body>

        <!-- Recall: all Bootstrap content must be enclosed in a container div -->
        <div class="container">
            
            <!-- Container is made of a series of rows -->
            <div class="row">
                
                <!-- Each row is divided into 12 units -->
                <!-- col-md-12 makes a column that spans all 12 units -->
                <div class="col-md-12">
                    OHAI DERE.
                </div>   <!-- /col-md-12 -->  
                
            </div> <!-- /row -->
            
        </div> <!-- /container -->
        
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </body>
    
</html>
```

Run the page and view it.

## Bootstrap Overview

Recall some basic facts about the Bootstrap grid system.

- Grid elements are created by making `div` tags and giving them `class` properties that describe the layout. Boostrap has a class
for almost everything you want to do.

- All Bootstrap grid elements must be enclosed in a `container` div. The container automatically pulls the content in from the left
and right edges a little bit.

- Within the container, the grid is organized into a series of `div` sections with `class="row"`.

- Each row is divided into 12 columns that span the full width of the container. You can group these 12 units into columns by creating
additional `div` elements within the `row`. In this example, the `col-md-12` class makes a column that spans all 12 units of its row. You can subdivide the 12 units in any way you want, such 6-6, 4-4-4, 3-6-3, 4-8, 11-1, etc., but **the units of all columns in 
the row must sum up to 12**.

- The `md` portion of the column class name controls the device size at which Bootstrap's grid stacking behavior takes effect (it can also be `sm`, `lg`, or `xl`). This is not important for us, but lets designers have more control over how the page appears on different-
sized mobile devices.

Let's modify the grid system. Change the single `col-md-12` `div` into two `div`s, each with `class=col-md-6`. This will create two
equal-width columns spanning the row. Put some text in each one and refresh your page.

## Jumbotron

The `jumbotron` class creates a top-level callout that can serve as a page heading. Add this text to the top of the body, above the
current `container`.

```
        <div class="jumbotron jumbotron-fluid bg-light">
           <div class="container">

                <!-- The display classes make text big -->
                <!-- display-1 is enormous, display-2 is huge, etc. -->
                <h1 class="display-4">
                    CMS 450 Meme Generator
                </h1>
               
               <!-- The lead class changes the font -->
               <p class="lead">
                   CHECK IT OUT WE MADE THIS IN LIKE AN HOUR
               </p>
            </div> <!-- container -->
        </div>
```

The basic jumbotron class is `jumbotron`, which is required. The `jumbotron-fluid` class makes it span the entire page width and
`bg-light` sets the background color to light gray.

The `jumbotron-fluid` class is slightly different from the normal grid system: the `container` goes *inside* the jumbotron.

How do you figure things like this out? **You consult the documentation**. Modern web programming isn't really about knowing clever
algorithms that you can whip out off the top of your head. It's more about combining components of pre-built frameworks and APIs to
get the effects you want. This requires researching the features that each framework implements.

## Canvas

`canvas` is an HTML5 element that supports drawing operations. Change the main `container` section within your `body` to the following:

```
        <div class="container">
            <div class="row">
                
                <div class="col-md-6">
                    <canvas id="canvas" width="640" height="480">
                        Sorry, your browser doesn't support the &lt;canvas&gt; element.
                    </canvas>
                </div> <!-- /col-md-6 -->
                
                <div class="col-md-6">
                    <h1> Controls Here </h1>
                </div> <!-- /col-md-6 -->

            </div> <!-- /row -->
        </div> <!-- /container -->
```

The left pane contains the canvas element, which is where the image will appear. The right pane will eventually contain the controls
for the application. If you refresh the page after saving, you won't see anything yet, because the `canvas` is blank by default.

Note that the `canvas` is set to 640 x 480. This is an absolute size in pixels. To work with Bootstrap, the `canvas` should fill its
entire containing column. Update the `head` section of the page to add a style rule that gives `canvas` 100% width.

```
    <head>
        
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

        <style>
            canvas {
                width: 100%;  /* canvas fills its parent column */
                height: auto;  /* canvas height is set proportional to width */
            }
        </style>
        
    </head>
```

Finally, add a `script` tag to the bottom of the body, above the current `script` tags, to load and draw an image on the canvas.

```
        <script>
            // Get a reference to the canvas's drawing context
            // context provides all drawing functions
            var canvas = document.getElementById("canvas");
            var context = canvas.getContext("2d");
            
            // Create a new Image and assign it a source URL
            var img = new Image();
            img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ducreux1.jpg/1280px-Ducreux1.jpg";
            
            // You can't draw the image until it's loaded
            // This function runs when the image is ready
            img.onload = function() {
                // Set canvas size to image size
                // Scales canvas up if image is larger than default in either dimension
                canvas.width = 640;
                canvas.height = 480;
                canvas.width = Math.max(canvas.width, img.width);
                canvas.height = Math.max(canvas.height, img.height);
                
                // Draw the image
                // (0, 0) is the upper-left corner of the canvas
                context.drawImage(img, 0, 0, img.width, img.height);
            }
        </script>
```

There are three steps here:

1. Get a reference to `canvas` using `document.getElementById`; this is our basic move. The second line gets a drawing context, which
is what we'll use to actually put things on the canvas.

2. The next two lines create an `Image` object and assign it a `src` URL.

3. You can't, however, draw the image immediately, so the third section sets up a callback function that will run once the image 
finishes loading. The first lines increase the `canvas` size if necessary; the image will still be contrained to 100% of its column,
but it won't be cut off or stretched. The last line finally draws the image on the `canvas`.

## Add Controls

Let's add some meme controls. Update the right column to the following:

```
                <div class="col-md-6">
                    
                    <label for="imageURL">Image URL</label>
                    <input type="text" class="form-control" id="imageURL" placeholder="Enter the URL of the image you want to meme.">
                             
                    <label for="memeText" class="mt-4">Meme Text</label>
                    <input type="text" class="form-control" id="memeText" placeholder="Put your meme text here.">
                                        
                    <button class="btn btn-primary btn-block mt-4" type="button" id="generateButton">
                        Generate Meme
                    </button>
    
                </div> <!-- /col-md-6 -->
```

The `input` tag creates an input field and the `type` property specifies that it is a `text` input, so it appears as a text box
when the page renders.

All Bootstrap inputs should have the `form-control` class. Notice, also, that each input has an `id` and a `placeholder` property
that sets the initial text in the field.

The `label` tags set the text that appear above each input.

Use the `button` tag to create buttons. All Bootstrap buttons have the `btn` class. The additional classes are

- `btn-primary` to make the button use the default Bootstrap blue color. There are other options: try `btn-danger` for a red button.

- `btn-block` makes the button span the entire width of its column. Without that class, the button would be sized to fit its text.

- `mt-4` adds some vertical space between elements.

## Phase 1: Get the Image URL from the Input Box

First, modify the `<script>` to load the image when the user clicks the button:

```
        <script>
            // Get a reference to the canvas's drawing context
            // context provides all drawing functions
            var canvas = document.getElementById("canvas");
            var context = canvas.getContext("2d");
            
            // Get a DOM reference to the button
            var button = document.getElementById("generateButton");
            
            // Set a function that runs when the button is clicked
            button.onclick = function() {
            
                // Create a new Image and assign it a source URL
                var img = new Image();
                img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ducreux1.jpg/1280px-Ducreux1.jpg";
            
                // You can't draw the image until it's loaded
                // This function runs when the image is ready
                img.onload = function() {
                    // Set canvas size to image size
                    // Scales canvas up if image is larger than default in either dimension
                    canvas.width = 640;
                    canvas.height = 480;
                    canvas.width = Math.max(canvas.width, img.width);
                    canvas.height = Math.max(canvas.height, img.height);
                
                    // Draw the image
                    // (0, 0) is the upper-left corner of the canvas
                    context.drawImage(img, 0, 0, img.width, img.height);
                }
            }
        </script>
```

This is a basic technique: get a reference to a page element using `document.getElementById()`, then set its `onclick` property
to a function that runs when the user clicks on the element. In this case, the click function is the same code that loaded the
pre-set image.

Refresh the page and click the button. You should see the image load in the left pane.

Now, modify the `<script>` to read the URL from the `imageURL` box and set it as the `src` of the new image. Tips:

- Use `document.getElementById("imageURL")` to get a DOM reference to the text box.

- Access the `value` property to get the box's string.

Now, refresh the page, paste the URL into the input box, and press the button!

```
https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ducreux1.jpg/1280px-Ducreux1.jpg

https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/The_lake_of_Hakone_in_the_Segami_province.jpg/2560px-The_lake_of_Hakone_in_the_Segami_province.jpg
```

## Phase 2: A Meme is an Image with Text

Adding text to the image is conceptually easy:

- Read the meme text from the box.

- Draw it onto the image using the appropriate `context` functions.

Modify the `<script>` to add some static text:

```
        <script>
            // Get a reference to the canvas's drawing context
            // context provides all drawing functions
            var canvas = document.getElementById("canvas");
            var context = canvas.getContext("2d");
            
            var button = document.getElementById("generateButton");
            button.onclick = function() {
                
                // Get the source URL from the input box
                var inputBox = document.getElementById("imageURL");
                var url = inputBox.value;
            
                // Create a new Image and assign it a source URL
                var img = new Image();
                img.src = url;
            
                // You can't draw the image until it's loaded
                // This function runs when the image is ready
                img.onload = function() {
                    // Set canvas size to image size
                    // Scales canvas up if image is larger than default in either dimension
                    canvas.width = 640;
                    canvas.height = 480;
                    canvas.width = Math.max(canvas.width, img.width);
                    canvas.height = Math.max(canvas.height, img.height);                  
                
                    // Draw the image
                    // (0, 0) is the upper-left corner of the canvas
                    context.drawImage(img, 0, 0, img.width, img.height);
                    
                    // Set up and draw text
                    // Black outline first, then white filled
                    var text = "OHAI";
                    var textX = img.width / 2;  // Center text within image
                    var textY = img.height * .80;  // Place text near the bottom

                    var fontSize = .10 * img.width;  // Scale font based on image width                    
                    context.font = fontSize + "px Impact";  // Font string
                
                    context.textAlign = "center";  // Center text on x position
  
                    context.strokeStyle = 'black';
                    context.lineWidth = .10 * fontSize;  // Width of black outline
                    context.miterLimit = 2;  // Controls outline artifacts
                    context.strokeText(text, textX, textY);  // Write black outline

                    context.fillStyle = "white";
                    context.fillText(text, textX, textY);  // Write white text
                }
            }
        </script>
```

The new text drawing code is below the call to `context.drawImage`. The basic strategy is as follows:

- Draw the black outline first, then the white filled text. The important functions are `strokeText` and `fillText`. Each takes the 
string to write, plus the x and y position where it should be drawn on the `canvas`.

- The `canvas` API provides an option that makes centering text easy. Set `textAlign = "center"` and the text will appear centered around its input x position. In this example, the x value is set to the center of the image. The height is set to 80% of the image 
height, so the text appears close the bottom.

- The font size is scaled to 10% of the image width. This keeps the font about the same visual size regardless of the input image size. The black outline width is set to 10% of the font size, so it also scales proportionally.

- The font string combines the size in pixels with the font name, which is Impact for true meme authenticity.

Now modify the script to take the meme text from its input box. Again, use `document.getElementById` and the `value` parameter. 
When you've finished, you should be able to load an image by pasting its URL in the first box, then add text using the second box.

## Phase 3: Radio, Radio

This final example will demonstrate how to use radio buttons to select among mutually exclusive options. Our buttons will allow you
to place the text at either the top or the bottom of the image.

Modify the control pane to add Bootstrap-style radio buttons:

```
                <div class="col-md-6">
                    
                    <label for="imageURL">Image URL</label>
                    <input type="text" class="form-control" id="imageURL" placeholder="Enter the URL of the image you want to meme.">
                             
                    <label for="memeText" class="mt-4">Meme Text</label>
                    <input type="text" class="form-control" id="memeText" placeholder="Put your meme text here.">
                                          
                    <!-- Radio button group -->
                    <div class="btn-group btn-group-toggle mt-4" data-toggle="buttons">
                        <label class="btn btn-outline-primary active">
                            <input type="radio" name="positions" value="bottom" autocomplete="off" checked> Text at Bottom
                        </label>
                        <label class="btn btn-outline-primary">
                            <input type="radio" name="positions" value="top" autocomplete="off"> Text at Top
                        </label>
                    </div>
                                        
                    <button class="btn btn-primary btn-block mt-4" type="button" id="generateButton">
                        Generate Meme
                    </button>
           
                </div> <!-- /col-md-6 -->
```

The radio buttons have the class `btn-group`, which creates a set of buttons side-by-side. The `btn-group-toggle` class enforces the
behavior that only one can be active at any time. Clicking on one will select it and de-select the others in the group.

Each input is wrapped in an outer label, which has the class `btn-primary-outline`. This draws a white, unfilled button with blue text.
The first button as the class `active`, which makes it appear as the selected element. Both have the required `btn` class.

Notice that the buttons all have `type="radio"` and `name="positions"`. All radio buttons in a group have the same name. The first
one, which has the `active` class, also has the `checked` property set to indicate that it's selected.

Reload the page and experiment with clicking the buttons. You'll see that the one you click becomes active and the other is deactivated.

Finally, let's modify the script to check which button is active. Add this code in place of the line that sets `textY`.

```
                    // Select height using radio buttons
                    var position = document.querySelector('input[name="positions"]:checked').value;
                    if (position == "bottom") {
                        textY = img.height * .80;
                    } else {
                        textY = img.height * .20;
                    }
```

This shows an alternate way of getting a value from an element. `document.querySelector` will find an element matching specified properties and return it. In this case, the string specifies searching the `input` elements with the name `positions` (recall that all buttons in the radio group share this name), then returning the one that has the `checked` property, which will always be the one
that was clicked most recently.

The `if` statement sets the text height to be either close to the top or the bottom based on the position value.

## Save Teh Memez

If you want to save a meme, right-click (or CTRL + click on Mac) and choose "Save Image As..." to download as a PNG file.

## Complete Code

Here's the complete page with all elements and script features:

```
<!doctype html>
<html>
    
    <head>
        
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        
        <style>
            canvas {
                width: 100%;
                height: auto
            }
        </style>
    </head>
    
    
    <body>
        
        <div class="jumbotron jumbotron-fluid bg-light">
           <div class="container">

                <!-- The display classes make text big -->
                <h1 class="display-4">
                    CMS 450 Meme Generator
                </h1>
               
               <p class="lead">
                   CHECK IT OUT WE MADE THIS IN LIKE AN HOUR
               </p>
            </div> <!-- container -->
        </div>
        

        <!-- Recall: all Bootstrap content must be enclosed in a container div -->
        <div class="container">
            <div class="row">
                
                <div class="col-md-6">
                    <canvas id="canvas" width="640" height="480">
                        Sorry, your browser doesn't support the &lt;canvas&gt; element.
                    </canvas>
                </div> <!-- /col-md-6 -->
                
                <div class="col-md-6">
                    
                    <label for="imageURL">Image URL</label>
                    <input type="text" class="form-control" id="imageURL" placeholder="Enter the URL of the image you want to meme.">
                             
                    <label for="memeText" class="mt-4">Meme Text</label>
                    <input type="text" class="form-control" id="memeText" placeholder="Put your meme text here.">
                                          
                    <!-- Radio button group -->
                    <div class="btn-group btn-group-toggle mt-4" data-toggle="buttons">
                        <label class="btn btn-outline-primary active">
                            <input type="radio" name="positions" value="bottom" autocomplete="off" checked> Text at Bottom
                        </label>
                        <label class="btn btn-outline-primary">
                            <input type="radio" name="positions" value="top" autocomplete="off"> Text at Top
                        </label>
                    </div>
                                        
                    <button class="btn btn-primary btn-block mt-4" type="button" id="generateButton">
                        Generate Meme
                    </button>
           
                </div> <!-- /col-md-6 -->

            </div> <!-- /row -->
   
        </div> <!-- /container -->
        
        <script>
            // Get a reference to the canvas's drawing context
            // context provides all drawing functions
            var canvas = document.getElementById("canvas");
            var context = canvas.getContext("2d");
            
            var button = document.getElementById("generateButton");
            button.onclick = function() {
                
                // Get the source URL from the input box
                var inputBox = document.getElementById("imageURL");
                var url = inputBox.value;
            
                // Create a new Image and assign it a source URL
                var img = new Image();
                img.src = url;
            
                // You can't draw the image until it's loaded
                // This function runs when the image is ready
                img.onload = function() {
                    // Set canvas size to image size
                    // Scales canvas up if image is larger than default in either dimension
                    canvas.width = 640;
                    canvas.height = 480;
                    canvas.width = Math.max(canvas.width, img.width);
                    canvas.height = Math.max(canvas.height, img.height);                  
                
                    // Draw the image
                    // (0, 0) is the upper-left corner of the canvas
                    context.drawImage(img, 0, 0, img.width, img.height);
                    
                    // Set up and draw text
                    // Black outline first, then white filled
                    var text = document.getElementById("memeText").value;
                    var textX = img.width / 2;  // Center text within image
                    
                    // Select height using radio buttons
                    var position = document.querySelector('input[name="positions"]:checked').value;
                    if (position == "bottom") {
                        textY = img.height * .80;
                    } else {
                        textY = img.height * .20;
                    }
                    
                    var fontSize = .10 * img.width;  // Scale font based on image width                    
                    context.font = fontSize + "px Impact";  // Font string
                
                    context.textAlign = "center";  // Center text on x position
  
                    context.strokeStyle = 'black';
                    context.lineWidth = .10 * fontSize;  // Width of black outline
                    context.miterLimit = 2;  // Controls outline artifacts
                    context.strokeText(text, textX, textY);  // Write black outline

                    context.fillStyle = "white";
                    context.fillText(text, textX, textY);  // Write white text
                }
            }
        </script>
        
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </body>
    
</html>
```

## Lessons

Again, the purpose of this lab is **not** to memorize every feature and class we used to build the application. Keep the following things in mind:

- Modern web dev is mostly about gluing together components of frameworks and browser API calls to get the effects you want. **Everything in this project came from reading Bootstrap documentation or doing searches to find examples**.

- Remember the key technique of naming elements and then using `document.getElementById` to interact with them.

- There are a lot of `canvas` functions, but they're mostly boilerplate that comes, again, from reading documentation and doping searches for examples. Likewise with the Bootstrap classes: there is a class for almost every design feature you want, you just have to 
do a little reading to figure out what it is. The radio button example comes straight out of the Bootstrap documentation.

## Jam

If you have time, think about other features that might be cool to add. You could add some more buttons to the radio group, or try
automatically inserting line breaks into the text.
