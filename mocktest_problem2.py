__author__ = 'Kalyan'

# Score you will get if you pass all the tests.
max_marks = 25

problem_notes = '''
Find the Lowest common multiple of 2 positive numbers which are given in their prime factorized form defined in problem1

You must return the result in a valid prime factorized form as described in problem1.
Invalid results will fail the tests, so do pay attention to the definition of a valid factorization given in problem1.

Use python builtins and data types as you see fit.

For HCF and LCM: http://www.whitman.edu/mathematics/higher_math_online/section03.06.html

Notes:
1. Assume inputs are valid and of the the right type.
2. first and second are list of tuples which represent a number and they are in prime factorized form as described in
   problem1
'''

def get_lcm(first, second):
    x = 1
    y = 1
    for i in first:
        x = pow(i[0], i[1])
    for i in second:
        y = pow(i[0], i[1])
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    number = lcm
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
def test_get_lcm():
    assert [(2,1), (5,1)] == get_lcm([(2,1)], [(5,1)])
    assert [(3,2)] == get_lcm([], [(3,2)]) # empty list is 1
