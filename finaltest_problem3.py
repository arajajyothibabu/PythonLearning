__author__ = 'Kalyan'

max_marks = 20

problem_notes ='''
Write a routine to sort the given list of numbers according to the number
of prime factors it has.

Constraints:
1. 1 and 0 are considered to have 0 factors
2. For negative numbers, the factor count of the corresponding
   positive numbers is considered for sorting
3. Numbers with more factors come before numbers with fewer factors
4. In case of a tie, bigger numbers (numerically) comes first

Notes:
1. Write additional helper routines as required.
'''

# assume is numbers is a valid list of numbers
def is_prime(n):
    i = 2
    while i < abs(n):
        if n % i == 0:
            return False
        i += 1
    return True

def count_of_prime_factors(x):
    if x == 0 or x == 1:
        return 0
    i = 2
    c = 0
    while i < abs(x):
        if x % i == 0 and is_prime(i):
            c += 1
        i += 1
    return c


def sort_by_factor_count(numbers):
    if numbers == None:
        return None
    numbers.sort(key=count_of_prime_factors,reverse=True)
    i = 0
    while i < len(numbers)-1:
        if count_of_prime_factors(numbers[i]) == count_of_prime_factors(numbers[i+1]):
            if numbers[i] < numbers[i+1]:
                t = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = t
        i += 1
    print numbers
    return numbers

# one basic test given, write more exhaustive tests
def test_sort_by_factor_count():
    # 10 has 2 factors [2,5] , 6 has 2 [2,3], 8 has 1 [2] and 2 has 1 [2], hence the result
    assert [10, 6, 8, 2] == sort_by_factor_count([2, 8, 6, 10])
    assert [6,-10, 8, 2] == sort_by_factor_count([2, 8, 6, -10])
    assert [77,48,17,7] == sort_by_factor_count([17,77,48,7])


