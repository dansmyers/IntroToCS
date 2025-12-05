# Objects and Classes

## Topics

- Objects encapsulate related data
- A class is a template for creating objects

## Encapsulation

An object is a programming structure that contains a set of related variables and methods for operating on those variables. An object "wraps up", into a single unit, a set of variables that are logically-related to each other and then provides a set of methods that other parts of the program can use to interact with those variables.

If you want to be fancy, which you do, you can say that a class *encapsulates* data and allows controlled access to its data through its methods.

Consider a string:

- The data for the string is its sequence of characters
- Strings have a set of methods that you can use to perform operations on their data: `lower`, `upper`, `find`, `strip`, etc.
- But you can't reach inside a string and make arbitrary changes to its data; you can only interact with the string in the ways allowed by its pre-defined methods

Objects are useful as a way to manage complexity in larger programs. Object-oriented programming (OOP) decomposes the overall application into a collection of objects, each of which manages its own data. Objects interact with each other by calling methods to perform well-defined operations. This strategy allows programmers to ensure that groups of related variables are managed together and that variables are protected from arbitrary, unsafe, or logically invalid changes.

## Classes

A class is a template for creating objects of a particular type. A class block defines the properties and behaviors of a particular type of object.

For example, think about a position on a sports team, like a Forward. That class defines a certain set of roles and responsibilities for a particular player within the context of a team. A specific Forward, say Lionel Messi, is an **instance** of the general Forward class.

The Forward class might define certain variables represeting attributes that we would want to track and manage for a Forward, like goals scored, assists, shots, height, weight, etc. Messi, as an instance of the Forward class, has his personal assigned values of those variables. A different Forward, like Ronaldo, would have the same set of variables, but with his own assigned values.

You could also think of a class as being like a housing blueprint. Given a certain blueprint, a builder can construct many individual houses that are instances of the same basic design. Although the houses follow the same plan, each one has its own independent set of attributes for things like wall colors, flooring, and furnishings.

## Instantiating objects

The following program defines a class called `Book`, to represent a book with a title, author, and price.
```
"""
Define a class representing a Book
"""

class Book:
    """
    This block declares a Book class

    Right now, the block is just a placeholder, but we'll add more to it later
    """

    # The pass keyword indicates that this block is deliberately left empty for now
    pass


### Main

# Instantiate a Book object by calling its class name like a function
pnp = Book()

# Once the object is instantiated, assign values to its internal variables using dot notation
pnp.title = 'Pride and Prejudice'
pnp.author = 'Jane Austen'
pnp.price = 9.99

# Declare a second Book
dracula = Book()
dracula.title = 'Dracula'
dracula.author = 'Bram Stoker'
dracula.price = 5.99
```

The `class` keyword creates a block for a new class definition. By convention, class names are always *capitalized*. In this first example we're only declaring that a `class Book` exists. We haven't put any custom behaviors into the block yet, but we'll do that in the next note.

To instantiate an object, call its class name like a function:
```
pnp = Book()
```
This operation is called the **constructor method**. It tells Python to allocate memory for a new object of type `Book` and perform any required initialization steps.

You can create internal variables inside an object using dot notation:
```
pnp.title = 'Pride and Prejudice'
pnp.author = 'Jane Austen'
pnp.price = 9.99
```
These variables are called the *members*, *fields*, or *instance variables* of the object.

**Every object has its own copies of the instance variables**. Although we've used the names `title`, `author`, and `price` two times in the example code, they belong to separate objects and therefore distinct from each other. Think about each object being its own independent block of memory (because it is) containing the internal variables. The name of the object functions as a pointer to its underlying structure in memory.

```
           Book
           -------------------------------
          | title: 'Pride and Prejudice'  |
pnp ----> | author: 'Jane Austen'         |
          | price: 9.99                   |
           -------------------------------

               Book
               -----------------------
              | title: 'Dracula'      |
dracula ----> | author: 'Bram Stoker' |
              | price: 9.99           |
               -----------------------
```

