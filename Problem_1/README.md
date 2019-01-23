# Project Euler - Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

**Problem:** Find the sum of all the multiples of 3 or 5 below N.

## Solution: Explanation

The sum of all numbers between 1 and N which are divisible by 3 is

```math
s_{3} \ = \ 3+6+9+12+\dots +3i \ \ \text{where} \ 3i\leq N
```

```math
s_{3} \ = \ 3(1+2+3+\dots +i) \ \ \text{where} \ i\leq \frac{N}{3}
```

in summation notation,

```math
s_{3} \ = \ 3\bigg(\sum^{\frac{N}{3}}_{k=1} k\bigg)
```

using the formula for summing an arithmetic series we find

```math
s_{3} \ = \ 3\frac{(\frac{N}{3})(\frac{N}{3}+1)}{2}
```

Similarly, the sum of all numbers between 1 and N which are divisible by 5 is

```math
s_{5} \ = \ 5\frac{(\frac{N}{5})(\frac{N}{5}+1)}{2}
```

Therefore we can use the formula below to calculate the sum of all numbers below N divisible by 3 *and* 5. Note we have removed numbers divisible by 15 as they will appear twice.

```math
s \ = \ s_{3} + s_{5} - s_{15}
```
