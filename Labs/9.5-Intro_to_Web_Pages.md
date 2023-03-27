# Intro to Web Pages

## Overview

This short lab will let you practice jamming on simple HTML and CSS, two of the core technologies of front-end web programming. By the end of it, you should feel comfortable with the idea of representing web page content using tagged text and simple styling.

## Setup

Create a **new** repl.it workspace. Select the **HTML/CSS/JavaScript** template and name your workspace `CMS120-Web`.

## Write and Serve a Basic Web Page

### Creating the Page

Let's make a basic web page. 

Open up your new HTML/CSS/JS repl environment.

Put the following text in `index.html`. I'll tell you more about how this file is put together in the next section, after you've had the
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

Hit the "Run" button at the top of the screen to display your page.


### Page Contents

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

Before going further, experiment with making some changes to your page and visualizing the results. Run the server using `srv`, reload the page, then stop the server using CTRL + c (or COMMAND + c on Mac) when you need to make changes.


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

### Interior Decoration

Let's add an image to the page. The easiest way to add an image is to directly to it from your page. Add the following tag within the `<body>` region:

```
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg"/>
```

The `src` parameter supplies the URL of the image. Reload the page and check out your picture.

Yikes. That's large. You can add style to the tag to scale the image to a percentage of the display width:

```
<p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg" style="width:50%"/>
</p>
```

You can also set an absolute size in pixels, e.g. `"width:200px"`.

You can also serve images directly out of your project directory. The easiest way to do this is to first download them to your computer, then upload them back to repl.it. For example, if you had downloaded and the uploaded an image called `cheezburger.jpg`, you could add it your page using

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


### A Little CSS

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

### More Style Rules

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

**Fonts** The `font-family` parameter takes a list of fonts (a "font stack") and uses the first one that's available on the system. Here, the first choice font is Helvetica and the last choice is the default system sans-serif font, which is guaranteed to exist in every browser.`font-size` controls the size.

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
