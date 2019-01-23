def sum(n, k):
    d = n // k
    return k * (d * (d + 1)) // 2


def euler1(n):
    n = n - 1
    return sum(n, 3) + sum(n, 5) - sum(n, 15)


## Some simple tests

test_n1 = 100
test_n2 = 1000000000

print("Test case for n=100: ", euler1(test_n1))
print("Test case for n=1000000000: ", euler1(test_n2 - 1))

# run with py.test Problem1_Solution.py
def test_answer():
    assert euler1(10) == 23
