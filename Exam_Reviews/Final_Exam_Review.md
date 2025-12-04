# Final Exam Review

<img src="https://billiemag.ca/wp-content/uploads/2020/07/Colville_Dog-and-bridge.jpg" width="400px" />

*Alex Colville, Dog and Bridge (1976). Colville painted in the mid-20th Century, but his works look weirdly like low-res polygonal graphics from early 2000s PS2 games.

## Exam Details

The exam will be ~15 short answer questions. Every question will ask you to review a program or code fragment and predict its output. The overall purpose of the exam is to assess your mental model of how programs execute, which is an essential aspect of computational thinking.

Other information:

- No books, notes, internet access, or other resources
- No calculator; there won't be any calculations other than simple arithmetic
- **No trick questions**: every question has a straightforward answer
- The standard time limit is two hours

I will grade the exam by assessing the fraction of questions you answered correctly.

- If you score 80% or higher, you'll receive full credit
- If you score at least 60% but less than 80%, you'll receive half credit


## Tips

- Work through the questions below to practice most of the key concepts from the class. Claude is great for coming up with additional practice questions.
- Remember that you can always write a short program and run it to see what it does if you're unsure.
- Make notes to yourself. Trace the execution of the program step-by-step and keep track of the values of each variable.
- The examples below are not 100% exhaustive of every type of question that might be on the exam.
  

## Practice Questions

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
    x = x * 3
    return x    


def foo(value):
    x = baz(value + 2)
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
print(a[-1])
```


2. What is printed by this nested list operation?
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])
```

3. What is the output of this list slicing operation?
```
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
```


4. What is the output of the following program? Explain your answer.
```
a = [2, 10, 3, 9, 5, 8, 7, 7, 11]

for i in range(2, len(a), 2):
    if a[i] < a[i - 2]:
        print('False')
        quit()

print('True')
```

5. What is the output of the following function when the input is `"elastic"`. Explain your answer.
```
def has_no_a(word):
    for letter in word:
        if letter == 'a':
            return False
        else:
            return True
```

6. What is printed by the following access?
```
student = {
    'name': 'Alice',
    'grades': {'math': 90, 'science': 85}
}
print(student['grades']['science'])
```

7. What is the output of the following loop?
```
scores = {'math': 95, 'english': 88, 'history': 92}
for subject in sorted(scores.keys()):
    print(scores[subject])
```

### Misc.

1. What is the output of the following fragment? Recall that `ord` converts a character to its underlying numeric code and `chr` converts a code back to a character.
```
c = 'm'
code = ord(c) + 5
print(chr(code))
```

2. I wrote the following code but got an error when I tried to run it. What's the problem?
```
# Declare a point in 3-d space
point = (5, 7, 11)

# Update one coordinate
point[0] = 13
```

3. What is the output of the following object-oriented program?
```
class Car:
    def __init__(self, new_make, new_model, new_year):
        self.make = new_make
        self.model = new_model
        self.year = new_year

    def __str__(self):
        return f'{self.make} {self.model}, {self.year}'


c = Car('Honda', 'Accord', 2006)
print(c)
```
