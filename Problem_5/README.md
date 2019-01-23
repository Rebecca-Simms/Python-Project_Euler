# Project Euler - Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

**Problem:** What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to N?

## Solution Explanation

In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two integers *a* and *b*, usually denoted by `lcm(a,b)`, is the smallest positive integer that is divisible by both *a* and *b*. Since division of integers by zero is undefined, this definition has meaning only if *a* and *b* are both different from zero.

General formula for calculating *lcm(a,b)*:

![equation](https://latex.codecogs.com/gif.latex?lcm%28a%2Cb%29%20%5C%20%3D%20%5C%20%5Cfrac%7B%7Ca%5Ccdot%20b%7C%7D%7Bgcd%28a%2Cb%29%7D)

where *gcd(a,b)* is the greatest common divisor and is found using in the *fractions* python package.
