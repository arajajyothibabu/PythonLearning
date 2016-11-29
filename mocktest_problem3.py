__author__ = 'Kalyan'

# Score you will get if you pass all the tests.
max_marks = 25

problem1_notes = '''
Find the highest common factor of 2 positive numbers which are given in their prime factorized form defined in problem1

You must return the result in a valid prime factorized form as described in problem1.
Invalid results will fail the tests, so do pay attention to the definition of a valid factorization given in problem1.

Use python builtins and datatypes as you see fit.

For HCF and LCM: http://www.whitman.edu/mathematics/higher_math_online/section03.06.html

Notes:
1. Assume inputs are valid and of the the right type.
2. first and second are list of tuples which represent a number and they are in prime factorized form as described in
   problem1

'''

def gcd(a, b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def get_hcf(first, second):
    x = 1
    y = 1
    for i in first:
        x *= pow(i[0], i[1])
    for i in second:
        y *= pow(i[0], i[1])
    number = gcd(x, y)
    print number
    if number == 1:
        return []
    if number < 0:
        raise ValueError
    else:
        key = []
        val = []
        x = number
        while x != 0 and x != 1:
            i = 2
            while i <= x:
                while (x % i) == 0:
                    key.append(i)
                    x //= i
                i += 1
            if x > 1:
                key.append(x)
        key = list(set(key))
        for v in key:
            c = 0
            while number % v == 0 and number > 1:
                c += 1
                number /= v
            val.append(c)
        return zip(key,val)


# some basic tests given, write more according to given constraints.
def test_get_hcf():
    # hcf of 2 and 5 is 1
    assert [] == get_hcf([(2, 1)], [(5, 1)])
    # hcf of 4 and 6 is 2
    assert [(2, 1)] == get_hcf([(2, 2)], [(2, 1), (3, 1)])
