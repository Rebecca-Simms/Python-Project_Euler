def diffsquares(n):
    square1 = n*(n+1)*(2*n+1) // 6
    square2 = (n*(n+1) // 2)**2
    square_diff = abs(square1 - square2)
    return square_diff


n1 = 3

n2 = 10

n3 = 5948350

print("The sum square difference for natural numbers less than or equal to", n1, "is:", diffsquares(n1))
print("The sum square difference for natural numbers less than or equal to", n2, "is:", diffsquares(n2))
print("The sum square difference for natural numbers less than or equal to", n2, "is:", diffsquares(n3))



def test_answer():
    assert diffsquares(10) == 2640
