# Unsigned Integers

## Binary Numbers

Think about a number, any number. I like 4326. You can represent this number as a sum:

```
4326 = 4000 + 300 + 20 + 6
```

Each digit of the number corresponds to a multiple of a power of 10:

```
4326 = 4 * 10^3 + 3 * 10^2 + 2 * 10^1 + 6 * 10^0
```

Our traditional decimal number system, where each digit corresponds to a power of 10, is called the **base-10 number system**. We could also call it a *positional number system with radix 10*.

There's no reason, however, to restrict ourselves to a base-10 number system. Computers use a **base-2 number system**, also called the **binary number system**. Each position in a binary number corresponds to a power of 2, and each digit can take one of two values, 0 or 1. For example, the unsigned binary number 10111 can be converted into a decimal number by adding up the appropriate powers of 2:
```
10111 = 1 * 2^4 + 0 * 2^3 + 1 * 2^2 + 1 * 2^1 + 1 * 2^0
      = 16 + 4 + 2 + 1
      = 23
```
Try writing down a few strings of zeros and ones and converting them from binary to decimal, like in the example above.

Suppose you have an N digit unsigned binary number. What values can it represent? Answer: 0 to 2^N - 1, because an N-bit sequence can represent 2^N distinct values.

**Distinguishing Between Decimal and Binary**

Consider the number 1011. Is it decimal one-thousand-and-eleven, or binary eleven? The correct value will often be clear from the context, but if it isn't, it's conventional to append a little subscript to identify the base of the number.

For example, 1011<sub>2</sub> is a binary number. 1011<sub>10</sub> would be the decimal number one thousand and eleven.

### The Four-Digit Unsigned Binary Numbers

```
Binary    Decimal
------    -------
0000       0
0001       1
0010       2
0011       3
0100       4
0101       5
0110       6
0111       7

The rest of the table is left as an exercise...
```


## Binary Arithmetic

Add binary numbers the same way you add decimal numbers, with the complication that sums bigger than 1 require the carry of a 1 to the next column:

```
          1 <---- carrry
  1        1
+ 0     +  1
----    ------
  1       10
```

Here's the example of adding `0111` (decimal 7) and `0011` (decimal 3):

```
  111  <---- carries
  0111
+   11
-------
  1010
```

The binary multiplication algorithm is the same as the one for decimal multiplication. Here's the example of multiplying `100` (decimal 4) by `101` (decimal 5):

```
    100
  x 101
  ------
    100
   000
+ 100
---------
  10100
```

Think about how to perform binary subtraction and division.

## Converting Decimal to Binary

Converting binary to decimal is easy: just add up the relevant powers of 2, as in the examples above. Converting a decimal number into binary is slightly trickier.

Suppose you want to convert 74 into binary.
  - Start by finding the largest power of 2 that is **less than or equal to** 74: 64.
  
  - Take the difference: 74 - 64 = 10.
  
  - Repeat, finding the largest power of 2 that's less than or equal to 10: 8.
  
  - Take the difference again: 10 - 8 = 2.
  
  - Repeat again: the largest remaining power of 2 is 2 itself.
  
  - Take the difference: 2 - 2 = 0.
  
  - Write down 74 as a sum of powers of 2: 74 = 64 + 8 + 2.
  
  - Convert the sum into a binary number with 1's at the places corresponding to the powers of 2 in the sum: `1001010`.
    
Here's another example: 41.

  - The largest power of 2 smaller than 41 is 32.
  
  - 41 - 32 = 9
  
  - The largest power of 2 smaller than 9 is 8.
  
  - 9 - 8 = 1.
  
  - 1 is 2^0 and we're done.
  
  - Write down the sum: 41 = 32 + 8 + 1.
  
  - Convert to a binary number: `101001`.
    
## Hex

It's possible to use bases other than 10 and 2. In particular, the base-16, or **hexadecimal** number system is frequently used to represent longer bit strings.

Hex numbers use 16 digits, 0-9 and A-F to represent values from 0 to 15. **Each hex digit is equivalent to a four-bit unsigned binary number**.

```
Decimal    Binary    Hex
-------    ------    ---
0          0000      0
1          0001      1
2          0010      2
3          0011      3
4          0100      4
5          0101      5
6          0110      6
7          0111      7
8          1000      8
9          1001      9
10         1010      A
11         1011      B
12         1100      C
13         1101      D
14         1110      E
15         1111      F
```

A common use of hex is to encode bit strings in a more readable format. For example,

```
0110 1010 = 6A
1100 1011 0111 = CB7
```
