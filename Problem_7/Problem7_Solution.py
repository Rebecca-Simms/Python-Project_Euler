def isPrime(n):
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True




def number_prime(n):
    l = 0
    i = 2
    d = []
    while l < n:
        if isPrime(i):
            l += 1
            d.append(i)
        i += 1
    return d[n-1]


print("The 6th prime number is", number_prime(6))
print("The 1001st prime number is", number_prime(1001))

def test_answer():
    assert number_prime(6) == 13
    assert number_prime(1001) == 7927
