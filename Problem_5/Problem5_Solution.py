import fractions

# lcm = lowest common multiple, gcd = greatest common divisor
def lcm(n):
    ans = 1
    for i in range(1, n+1):
        ans = (ans*i)/fractions.gcd(ans, i)
    return int(ans)



def test_answer():
    assert lcm(10) == 2520
