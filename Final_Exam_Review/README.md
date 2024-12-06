# Final Exam Review

## Exam Details

The exam will be 15-20 short answer questions. Every question will ask you to review a program or code fragment and predict its output. The overall purpose of the exam is to assess your mental model of how programs execute, which is an essential aspect of computational thinking.

Other information:

- No books, notes, internet access, or other resources
- No calculator; there won't be any calculations other than simple arithmetic
- **No trick questions**: every program will have valid code that produces a straightforward answer
- The standard time limit is two hours

I will grade the exam by assessing the fraction of questions you answered correctly.

- If you score 80% or higher, you'll receive full credit
- If you score at least 60% but less than 80%, you'll receive half credit


## Practice Questions

### Variables and conditionals

1.  What is the output of the following code fragment?
```
x = 1.1111
y = x * 10
print(f'{y: .1f}')
```

2. What is the output of the following code fragment? Explain your answer.
```
if .1 + .2 == .3:
    print('Equal')
else:
    print('Not equal!?')
```

3. What is printed by the following program when the user inputs `5`?
```
user_input = input('Enter a positive integer: ')
x = int(user_input)

if x % 3 > 1:
    if (2 * x + 1) % 5 < 3:
        x = -x
    else:
        x = x ** 2

print(x) 
```

4. What is the output of the following program?
```
a = 5
b = 3
c = 2

z = (a + b + c) / 2 // 2
print(z)
```

5. What is the output of the following program?
```
a = True
b = False
c = True

x = a and b
y = a and not c
z = a and not b

print(x or y or not z)
```

### Functions

1. What is the output of the following program?
```
def area_of_circle(radius):
    return radius ** 2 * 3  # Use 3 for pi for calculation (lol)

print(area_of_circle(10))
```


2. The following function is supposed to return the minimum of the three inputs, but it's wrong. What is the output of the following program, *as written*?
```
def triple_min(a, b, c):
    """
    Return the maximum of the three inputs
    """
    if a < b:
        if a < c:
            return c
        else:
            return a
    else:
        if b < c:
            return c
        else:
            return b

print(triple_min(7, 3, 5))
```


3. What is the result produced by calling `weird(weird(11))`?
```
def weird(x):
    if x % 7 <= 3:
        return 2 * x + 1
    else:
        return x - 2
```

4. The following program will cause an error on the last line if you try to execute it. What is the problem?
```
def calculate_area(length, width):
    area = length * width
    return area

a = calculate_area(3, 4)
print(area)
```

5. What is printed by the following program?
```
def baz(x):
    x = x * 2
    return x    


def foo(value):
    x = baz(value + 1)
    return x


### Main
x = 1
x = foo(x)
print(x)
```

### Loops



1. What is the output of the following loop?
```
for i in range(20, 40):
    if i % 4 == 0:
        print(i)
```

2. What is the fifth number printed by the following pair of loops?
```
for a in [10, 20, 30]:
    for b in range(2, 5):
        print(a // b)
```

3. What will be printed by this loop that uses string multiplication?
```
for count in range(1, 5):
    print("*" * count)
```

4. What is the final output of this code fragment?
```
total = 0
for i in range(5):
    if i > 0:
        total += i * 2
    else:
        total += 1
print(total)
```

5. Give the numbers printed by this loop.
```
for num in range(15, 30, 3):
    if num % 2 == 0:
        print(num)
    else:
        print(num - 1)
```

6. Give the sequence of values printed by this loop.
```
x = 3
while x > 1:
    print(x)
    if x % 2 == 0:
        x = x / 2
    else:
        x = 3 * x + 1
```

<img src="https://imgs.xkcd.com/comics/collatz_conjecture.png" width="300px" />


### Lists and dictionaries

1. What is the output of the following fragment?
```
a = [i for i in range(1, 12, 3)]
print(a[-2])
```

2. What is the final list at the end of the following code fragment?
```
# Create an empty list
dinosaurs = []

# Add some dinos
dinosaurs.append("T-Rex")
dinosaurs.append("Triceratops")
dinosaurs.append("Stegosaurus")
dinosaurs.append("Plesiosaurus")
dinosaurs.append("Deinonychus")

# Oops! Plesiosaurus is a marine reptile, not a dinosaur!
dinosaurs.pop(3)

# Remove T-Rex from index 0 and store it
trex = dinosaurs.pop(0)

# Insert T-Rex back at index 3
dinosaurs.insert(3, trex)

# Insert Brachiosaurus at the start (index 0)
dinosaurs.insert(0, "Brachiosaurus")

# Insert Pachycephalosaurus at index 2
dinosaurs.insert(2, "Pachycephalosaurus")
```

3. What is printed by this nested list operation?
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])
```

4. What is the output of this list slicing operation?
```
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
```


5. What is the output of the following program? Explain your answer.
```
a = [2, 10, 3, 9, 5, 8, 7, 7, 11]

for i in range(2, len(a), 2):
    if a[i] < a[i - 2]:
        print('False')
        quit()

print('True')
```

6. What is the output of the following function when the input is `"elastic"`. Explain your answer.
```
def has_no_a(word):
    for letter in word:
        if letter == 'a':
            return False
        else:
            return True
```

### Classes and objects
