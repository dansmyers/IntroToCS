# Constructor and String Methods

## Topics

- Custom constructors for classes using `__init__`
- Printing an object
- The `__str__` method

## Review: Key ideas of OOP

Recall that an *object* is a programming structure that *encapsulates* a group of related variables. Objects provide *methods* that other parts of the program can call to interact with their data. *Object-oriented programming* is a paradigm that breaks the program up into a collection of "things" that can be well-modeled using objects. OOP is popular in many domains because it provides one effective way of decomposing a large problem into independent components and gives developers tools for capturing real-world relationships in their code.

A *class* is a template for creating objects of a certain type. A class defines the data and behaviors that are associated with a particular kind of object. We say that an object is *an instance of* its class.

## Constructors

Previously, we looked a simple `Book` class. We could instantiate `Book` objects by calling the name of the class like a function, then creating fields for the object using dot notation.
```
Book pnp = Book()
pnp.title = 'Pride and Prejudice'
pnp.author = 'Jane Austen'
pnp.price = 9.99
```
The call `Book()` is the special **constructor method** that tells Python to instantiate a new object of type `Book`.

The default constructor just allocates memory to make a new empty container object that can then be assigned new data. It's often desirable, though, to have a custom constructor that can set an object's fields and perform any required initialization steps during the construction process.

When Python sees a call to a class constructor like `Book()`, it checks inside the class for a special method named `__init__`. If the method is defined, then Python will use it to initialize the new object. Here's an updated version of the `Book` class with a custom `__init__` method.
```
"""
Define a class representing a Book
"""

class Book:
    """
    Version 2 with a custom constructor
    """

    def __init__(self, new_title, new_author, new_price):
        self.title = new_title
        self.author = new_author
        self.price = new_price

### Main

# Custom constructor that takes inputs for the object's fields
pnp = Book('Pride and Prejudice', 'Jane Austen', 9.99)

# Construct a second Book
dracula = Book('Dracula', 'Bram Stoker', 5.99)
```

In this version, the calls to `Book` in the main section take three inputs that are the title, author, and price of the new `Book`.

## `self`

Observe that the first input to `__init__` is the special keyword `self`, which is the **object self-reference**. Every method defined in a `class` block must have `self` as its first parameter. Notice that the calls to `Book` don't supply any special input in the first position; `self` is passed in *automatically* when you call a class method.

`self` is used to refer to an object's internal data from within its own code. In this case, we want to construct a new object and assign values to its internal fields using the three inputs `new_title`, `new_author`, `new_price`.

- `self.title` refers to a `title` field of the new object that's currently being constructed
- Likewise for `self.author` and `self.price`; they refer to the internal data fields of the new object that `__init__` is constructing

I like to name my constructor inputs using the `new_` format, to make it clear that the input is a value assigned to a new object, but this isn't required. You can use any variable name that makes sense.

## Printing an object

Suppose that you want to print objects
```
print(pnp)
print(dracula)
```
If you add these lines to the program above and run it, the output will probably not be what you expect:
```
<__main__.Book object at 0x7e3bd40afec0>
<__main__.Book object at 0x7e3bd40afef0>
```
By default, printing an object doesn't print its data. Instead, it prints the *memory address* where the object is stored. This is usually not what you want, although it does allow us to see that `pnp` and `dracula` refer to different objects that are at two different memory locations (observe that the addresses are slightly different).

## Custom printing

A classmay define a custom printing method called `__str__`. When you print an object, Python checks its class for the `__str__` method. The method **returns** a string representation of the object's data, which is then used as the output of `print`.

Here's an updated class with an `__str__` method. Notice that `self` is still the first input to `__str__`, because it's required for class methods.
```
"""
Define a class representing a Book
"""

class Book:
    """
    Version 3 with custom to-string method
    """

    def __init__(self, new_title, new_author, new_price):
        self.title = new_title
        self.author = new_author
        self.price = new_price

    def __str__(self):
        # Use formatting to build a return string that contains
        # this object's internal data
        return f'{self.title} by {self.author}, {self.price}'

### Main

# Custom constructor that takes inputs for the object's fields
pnp = Book('Pride and Prejudice', 'Jane Austen', 9.99)

# Construct a second Book
dracula = Book('Dracula', 'Bram Stoker', 5.99)

# Print: calls __str__ behind the scenes and prints what it returns
print(pnp)
print(dracula)
```

Notice that `__str__` doesn't print anything! It always *returns* a string representation of the object, which is then used as the output of `print`.
