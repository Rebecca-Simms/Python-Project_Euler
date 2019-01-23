def prime_factors(n):
    p = 2
    while n >= p*p:
        if n % p == 0:
            n = n // p
        else:
            p += 1
    return n


n1 = 100
n2 = 10001
n3 = 1345629482

print("Largest Prime Factor of", n1, "is", prime_factors(n1))
print("Largest Prime Factor of", n2, "is", prime_factors(n2))
print("Largest Prime Factor of", n3, "is", prime_factors(n3))

def test_answer():
    assert prime_factors(100) == 5
