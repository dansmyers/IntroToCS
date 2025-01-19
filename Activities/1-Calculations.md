# Calculation Practice

## Overview

This short activity will give you a few practice problems that you can use to try out calculations and printing in Python.

Use the basic arithmetic operators, numbers, and `print` to answer each of the following questions.


## McChocolate Potatoes

The Japanese yen currently trades for about $.0064.

I'm a sucker for regional fast food items. It turns out that you ~can~ could get **chocolate fries** at [McDonald's in Japan](https://www.eater.com/2016/1/19/10790586/mcdonalds-chocolate-fries-japan) (they are officially known
as "McChocolate Potatoes"). Are they any good? Maybe not, but they cost only 330 yen as a side item.

<img src="https://cdn.vox-cdn.com/thumbor/WMJG04bu5nCmDiQ5mh0_chXelTY=/247x0:787x405/1820x1213/filters:focal(247x0:787x405):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/48592139/McDonald_s_Chocolate_Fries.0.0.jpg" width="50%" />


Tips:

- Use a print statement that outputs the result of the calculation
- Use a comment to explain the purpose of the program

```
# Cost of a side of chocolate fries in dollars

print(330 * .0064)
```

### Thoughts

Right away, you might notice that it would be nice to have more context around the answer. For example, we might want to specify that it's in US dollars, or print to only two decimal places.

Don't worry. We'll add those features soon. For now, just focus on printing the results of the calculations as they appear.

## Kilos

One kilogram is equal to 2.20462 pounds.

The largest cocaine bust in American history occurred in [2019 at the Philadelphia Packer Marine Terminal](https://en.wikipedia.org/wiki/2019_Philadelphia_Packer_Marine_Terminal_cocaine_seizure). Customs officials seized 39,525 pounds of cocaine with an estimated street value of more than $1.3 billion. How many kilograms is that?

Tip:

- Code the number of pounds as `39525`. Python doesn't want commas in large numbers.
- You have a number of pounds and want to convert to kilos, so you need to *divide* by 2.20462.

Always sanity-check your output and verify that it seems reasonable. If you convert pounds to kilos, but get a number more than twice as large, you know that you did something wrong.
