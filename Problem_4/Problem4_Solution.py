def is_pali(x):
    num = str(x)
    return (num == num[::-1])

# finds a list of all palindrome made up of two 6-digit numbers.
def list_of_palindromes():
    palindromeList = []
    for i in range(100 ,1000):
        for j in range(100, 1000):
            if is_pali(i*j):
                palindromeList.append(i*j)
    return palindromeList

# assign variable for list of all palindromes
pali_list = list_of_palindromes()


def largest_pali(n):
    largest = 0
    for i in pali_list:
        if i < n and i > largest:
            largest = i
    return largest


n1 = 100000
n2 = 546734
n3 = 987499

print("Largest palindromic 6-digit number below", n1, "is:", largest_pali(n1))
print("Largest palindromic 6-digit number below", n2, "is:", largest_pali(n2))
print("Largest palindromic 6-digit number below", n3, "is:", largest_pali(n3))

def test_answer():
    assert largest_pali(101102) == 101101
