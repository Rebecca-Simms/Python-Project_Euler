def even_fibonacci_sum(n):
    a = 1
    b = 1
    even_sum = 0
    while True:
        c = a + b
        if c >= n:
            return even_sum
        if c % 2 == 0:
            even_sum += c
        a, b = b, c



def test_answer():
    assert even_fibonacci_sum(10) == 10
