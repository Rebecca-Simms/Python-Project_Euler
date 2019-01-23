# Project Euler - Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is, *1^2 + 2^2 + .. + 10^2 = 385*. The square of the sum of the first ten natural numbers is,
*(1+2+..+10)^2 = 55^2 = 3025*. Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the sum is *3025-385=2640*.

**Problem:** Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.

## Solution Explanation:

Using the formula for a triangular number we can use:

![equation](https://latex.codecogs.com/gif.latex?%5Csum%20x%20%3D%20%5Cfrac%7Bx%28x&plus;1%29%7D%7B2%7D)

There is also a mathematical formula for the square pyramidal number:

![equation](https://latex.codecogs.com/gif.latex?%5Csum%20x%5E2%20%3D%20%5Cfrac%7Bx%28x&plus;1%29%282x&plus;1%29%7D%7B6%7D)

Use both of these equations to calculate the sum square difference. 
