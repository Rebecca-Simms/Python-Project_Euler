import time

def SieveOfEratosthenes(n):
    """ Create a boolean array "prime[0..n]" and initialize
        all entries it as true. A value in prime[i] will
        finally be false if i is not a prime, else true.
    """
    prime = [True for i in range(n + 1)]
    prime2 = []
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p to False
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    # return all prime numbers (all values which are still True)
    for p in range(2, n):
        if prime[p]: # True
            prime2.append(p)
    return prime

def sum_of_primes(p):
    """ Take list of primes found in SieveOfEratosthenes and create a new list of summed primes
        where summation[i] is all primes summed up to i.
    """
    summation = [0] * len(p)
    summation[0] = summation[1] = 0
    summation[2] = 2
    for i in range(3, len(summation)):
        if p[i] is True:
            summation[i] = summation[i-1] + i
        else:
            summation[i] = summation[i-1]
    return summation



# Checking how long algorithm takes

start_time = time.clock()

primes = SieveOfEratosthenes(1000000)

s = sum_of_primes(primes)

# test cases

print(s[5])
print(s[10])
print(s[100])
print(s[34536])

print(time.clock() - start_time, "seconds")  # 0.372073 seconds

###

def find_sum(i):
    s = sum_of_primes(primes)
    return s[i]

def test_answer():
    assert find_sum(10) == 17
