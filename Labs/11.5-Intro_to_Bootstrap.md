# Introduction to Bootstrap

## Background

Boostrap was originally developed by Mark Otto and Jacob Thornton at Twitter and was released as an open-source framework in 2011.

Bootstrap's main use is creating responsive, grid-based layouts. It provides convenient tools for dividing your page up into a layout of rows and columns and can automatically
adjust the layout based on the size of the viewing window, which is important for creating mobile-first sites. The framework also includes a set of style defaults that are 
better than your browser's bare HTML.

## Basic Bootstrap Layout

Here is an example HTML page that shows off the basic elements of Bootstrap. Open up your Mimir workspace, and create a new HTML file called `bootstrap_example.html`. Copy the 
code below, save the page, then serve it using `srv` (review the first HTML lab if you need to refresh how to view pages on Mimir).

```
<!doctype html>
<html>
    
    <head>
        
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        
    </head>
   
    <body>

        <!-- All Bootstrap content must be enclosed in a container div -->
        <div class="container">
            
            <!-- The container must contain one or more row divs -->
            <div class="row">
            
                <div class="col-6">
                    This is the left column.
                </div>   <!-- /col-6 -->  
                
                <div class="col-6">
                    This is the right column.
                </div>   <!-- /col-6 -->  
                
            </div> <!-- /row -->
            
        </div> <!-- /container -->
        
        <!-- JS, Popper.js, and jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    </body>
    
</html>
```

Let's start by pointing out a few important things in this example.

### CDN Links

There is a link to the bootstrap CSS stylesheet in the `<head>` section. Similarly, there are three required JavaScript files being loaded at the bottom of `<body>`. Any HTML file you create that uses Bootstrap will contain these links at the same locations.

It's possible to setup your project so that the required files are hosted locally, rather than being loaded from a remote CDN site,
but we're going to stick with the link-based setup for now.

### `<div>` Tags

The page is made up of a series of `<div>` tags. Think of each `<div>` as representing a "division" of the page. By itself, `<div>` just functions like a `<p>` tag: it's main
purpose is to allow you to create **a named region of the page** that you can style and interact with.

**Everything** in Bootstrap runs off of `<div>` tags with attached class labels. If you want to do something in Bootstrap, there's a 90% chance you're going to do it by making
a `<div>` and then adding class labels that control the effect you want.

The downside of this approach is that you end up making a lot of `<div>` tags. Notice how I've used comments to mark the closing of each `<div>`: you want to do that or you'll
quickly get lost.

### Containers

Take a look at the first `<div>` inside the `<body>`. It has class label `container`.

**All page content must be inside a container**. Let me say that again: ***ALL PAGE CONTENT MUST BE INSIDE A CONTAINER***.

(Where must all page content be? ***INSIDE ONE TOP-LEVEL CONTAINER***.)

As you lay out the page, you're going to create additional rows and columns, discussed in more detail below, but everything you create must be enclosed by one top-level
container `<div>`.


### Rows and Columns

Bootstrap models the page as a series of one or more **rows**, with each row subdivided into **columns**.

Here is the core content from the example above:

```
        <!-- All Bootstrap content must be enclosed in a container div -->
        <div class="container">
            
            <!-- The container must contain one or more row divs -->
            <div class="row">
            
                <div class="col-6">
                    This is the left column.
                </div>   <!-- /col-6 -->  
                
                <div class="col-6">
                    This is the right column.
                </div>   <!-- /col-6 -->  
                
            </div> <!-- /row -->
            
        </div> <!-- /container -->

```

Inside the top-level container is a `<div>` with the class `row`. Inside that `<div>` are two columns, both with the class label `col-6`.

### The Twelve Columns

Bootstrap subdivides each row into **twelve equally spaced column units**. You can create column combinations that span any subset of the twelve column units.
In the example above, each column is labeled `col-6`: the two columns each span six of the twelve units and divide the page in half.

```
                          Full row spans 12 units
 -------------------------------------------------------------------------
|                                                                         |
v                                                                         v
 ------------------------------------ ------------------------------------
|                                    |                                    |
|               col-6                |               col-6                |
|                                    |                                    |
 ------------------------------------ ------------------------------------
```

You can use any combination of `col` classes to divide the row in any way that you want. For example, three four-unit columns will split the row into
thirds:

```
 ------------------------ ------------------------ ------------------------
|                        |                        |                        |
|         col-4          |         col-4          |         col-4          |
|                        |                        |                        |
 ------------------------ ------------------------ ------------------------
```

Creating unequal-width columns is useful:

```
 ------------------------------------------------- ------------------------
|                                                 |                        |
|                     col-8                       |         col-4          |
|                                                 |                        |
 ------------------------------------------------- ------------------------
```

Spanning all twelve units fills the entire row:

```
 --------------------------------------------------------------------------
|                                                                          |
|                                 col-12                                   |
|                                                                          |
 --------------------------------------------------------------------------
```

### Practice

Go back to your example on Mimir and edit the columns to create some different combinations.

Once you have tried two columns, and a third `<div>` (make sure it's within the row) and experiment with three-column layouts.

## Important Layout Rules (How to Not Screw Everything Up)

There are four layout rules that you must remember **and never violate** or terrible things will happen:

1. Everything must go into one top-level container `<div>`.

2. The only things that can be within the container are one or more rows.

3. Each row must contain one or more columns that span a total of twelve units.

4. The actual page content must only be placed within columns. 

Most Bootstrap layout errors are caused by violating the `container -> row -> column -> content` nesting rules. In particular, if you try to place page content outside of the
`container -> row -> column` structure, it will probably look like it's hanging in space, disconnected from the rest of the page layout.

**A super common error** is to put content in a row without declaring a column. You'd think this should work, but it doesn't.

If you spend some time reading other Bootstrap documents, you'll learn that there are cases where these rules can be relaxed. Notably, Bootstrap is smart enough to figure out
how to automatically space your columns in many cases, which can simplify how you declare your columns. For now, I recommend manually allocated all twelve units in each row
while you're getting comfortable with the layout rules.


## More Practice

Take a look at `hokusai.html`, which shows off a few more features. Load it into Mimir, view it with `srv`, then experiment with modifying it.

### Responsive Layouts

Once you have the page up and running, experiment with changing the size of your browser. You should see the page content automatically shrink, then stack as the window gets smaller.

Bootstrap lets you control how the stacking behavior takes effect by adding size information to the column labels. In the `hokusai.html` file, you'll see columns labeled
with classes like `col-lg-8`. Here, the `lg` controls when the stacking behavior kicks in: specifically, it indicates that Bootstrap should start to stack the columns when the viewing window is smaller than 992 pixels, which is what Bootstrap considers to be "large". There are also `md`, `sm`, and other versions of the column classes that turn on stacking at different window sizes.

You don't need to memorize anything about the stacking behavior or the window sizes, but simply take comfort in knowing that it's one thing you can control in these turbulent times.
