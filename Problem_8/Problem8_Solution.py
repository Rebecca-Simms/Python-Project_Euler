def get_Groups(N, k):
    """ This function takes an 'N' digit number and returns
        all the possible combinations of 'k' consecutive numbers.
    """
    N = str(N)
    list_of_nums = []
    for num in N:
        list_of_nums.append(int(num))
    length_list = len(list_of_nums)
    combinations = [] #possible combinations of 'k' numbers
    i = 0
    while i < (length_list - (k-1)):
        possible_combs = list_of_nums[i:i+k]
        combinations.append(possible_combs)
        i += 1
    return combinations


def multiplyList(myList):
    """ This takes all the numbers in a list and multiplies them together.
    """
    result = 1
    for x in myList:
        result = result * x
    return result

def find_products(combinations):
    """ Applied multiplyList function to every possible combination of k numbers,
        which is in itself a list.
    """
    products = []
    for comb in combinations:
        products.append(multiplyList(comb))
    return products


def max_product(prod):
    """ Finds max in list of products.
    """
    max = 0
    for i in prod:
        if i > max:
            max = i
    return max


def largest_prod_in_series(n,k):
    """ Combines all functions together to find result.
    """
    combinations = get_Groups(n, k)
    products = find_products(combinations)
    return max_product(products)



def test_answer():
    assert largest_prod_in_series(2019060606, 5) == 0
