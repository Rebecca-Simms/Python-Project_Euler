# Project Euler - Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

**Problem:** Find the sum of all the multiples of 3 or 5 below N.

## Solution: Explanation

The sum of all numbers between 1 and N which are divisible by 3 is

![equation](https://latex.codecogs.com/gif.latex?s_%7B3%7D%20%3D%203&plus;6&plus;9&plus;12&plus;%5Cdots%20&plus;3i%20%5C%20%5C%20%5Ctext%7Bwhere%7D%20%5C%203i%5Cleq%20N)

![equation](https://latex.codecogs.com/gif.latex?s_%7B3%7D%20%5C%20%3D%20%5C%203%281&plus;2&plus;3&plus;%5Cdots%20&plus;i%29%20%5C%20%5C%20%5Ctext%7Bwhere%7D%20%5C%20i%5Cleq%20%5Cfrac%7BN%7D%7B3%7D)

in summation notation,

![equation](https://latex.codecogs.com/gif.latex?s_%7B3%7D%20%5C%20%3D%20%5C%203%5Cbigg%28%5Csum%5E%7B%5Cfrac%7BN%7D%7B3%7D%7D_%7Bk%3D1%7D%20k%5Cbigg%29)

using the formula for summing an arithmetic series we find

![equation](https://latex.codecogs.com/gif.latex?s_%7B3%7D%20%5C%20%3D%20%5C%203%5Cfrac%7B%28%5Cfrac%7BN%7D%7B3%7D%29%28%5Cfrac%7BN%7D%7B3%7D&plus;1%29%7D%7B2%7D)

Similarly, the sum of all numbers between 1 and N which are divisible by 5 is

![equation](https://latex.codecogs.com/gif.latex?s_%7B5%7D%20%5C%20%3D%20%5C%205%5Cfrac%7B%28%5Cfrac%7BN%7D%7B5%7D%29%28%5Cfrac%7BN%7D%7B5%7D&plus;1%29%7D%7B2%7D)

Therefore we can use the formula below to calculate the sum of all numbers below N divisible by 3 *and* 5. Note we have removed numbers divisible by 15 as they will appear twice.

![equation](https://latex.codecogs.com/gif.latex?s%20%5C%20%3D%20%5C%20s_%7B3%7D%20&plus;%20s_%7B5%7D%20-%20s_%7B15%7D)
