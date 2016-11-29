__author__ = 'Kalyan'

# Score you will get if you pass all the tests.
max_marks = 25

problem_notes = '''
Convert the passed in positive integer number into its prime factorization form.

If number = a1 ^ p1 * a2 ^ p2 ... where a1, a2 are primes and p1, p2 are powers >=1 then we represent that using lists
and tuples in python as [(a1,p1), (a2,p2), ...]

Note that a1 < a2 < ... and p1, p2 etc are all >= 1.

For e.g.
 [(2,1), (5,1)] is the correct prime factorization of 10 as defined above.
 [(5,1), (2,1)] is invalid as the the order is not correct.
 [(2,1), (3,0), (5,1)] is invalid as a prime with power 0 is present in the result.

Notes
0. This problems asks for explicit type checking!
1. Corner case 1 is represented as an empty list: []
2. Non positive numbers should raise a ValueError
3. If the type of number is not int or long raise a TypeError

Write simple brute force code.
'''
def factorize_number(number):
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
def test_factorize_number():
    assert [] == factorize_number(1)
    assert [(2,1)] == factorize_number(2)