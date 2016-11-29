__author__ = 'Araja Jyothi Babu'

def lcm(a, b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    if y == 0:
        return 0
    if x % y == 0:
        return x
    else:
        z = x
        while True:
            if z % x == 0 and z % y == 0:
                return z
            z += 1
        return z


def test_lcm():
    assert 10 == lcm(5,10)
    assert 0 == lcm(0,0)
    assert 8 == lcm(4,8)
    assert 4032 == lcm(64,63)


def gcd(a, b):
    if a >= b:
        x = a
        y = b
    else:
        x = b
        y = a
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def test_gcd():
    assert 5 == gcd(5,10)
    assert 0 == gcd(0,0)
    assert 4 == gcd(4,8)
    assert 1 == gcd(64,63)