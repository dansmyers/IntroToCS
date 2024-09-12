# Dice Games

## Passe-Dix

Passe-dix (French for "pass ten") is an ancient dice game. According to some early gambling books, it was allegedly the game played by Roman soldiers to divide the clothes of Jesus at the Crucifixion. The rules are simple: roll three dice and add their sum. The player wins if the sum is strictly greater than 10, loses if the sum is strictly less than 10, and draws ("pushes" in gambling terms) if the sum equals 10.

Write a program that implements passe-dix. Here is example output:

```
The dice are 2, 5, and 1.
The sum is 8.
You lose.
```

Your program should use `randint` three times to generate the three die rolls. Assign each roll to its own variable. Calculate the sum, then use an `if`-`elif`-`else` block to test for the three conditions.
