import math


def pythag(n):
    poss = [-1,]
    for b in range(2, (n // 3) + 1):
            a = (n**2 - 2*n*b) / (2*(n-b))
            if a % 1 == 0:
                c = n - a - b
                poss.append(int(a * b * c))
    return max(poss)



print(pythag(2990))  # 603232500
print(pythag(2991))  # -1
print(pythag(2992))  # 946833360
print(pythag(2993))  # -1
print(pythag(2994))  # -1
print(pythag(2995))  # -1
print(pythag(2996))  # -1
print(pythag(2997))  # -1
print(pythag(2998))  # -1
print(pythag(2999))  # -1
print(pythag(3000))  # 937500000


def test_answer():
    assert pythag(12) == 60
