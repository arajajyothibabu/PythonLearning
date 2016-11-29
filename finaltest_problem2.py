__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the letters a to e are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ca", decimal 5 is "ba" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int or long raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [a to e].
def convert(n):
    result = {i: chr(97+i) for i in range(5)}
    return result[n]


def reverse_of_number(n):
    s = 0
    while n > 0:
        s = s * 10 + n % 5
        n /= 5
    return s



def to_custom_base5(number):
    result = []
    x = 0
    while number > 0:
        x = number % 5
        result.append(convert(x))
        number /= 5
    result.reverse()
    return "".join(result)



# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.
def base5_to_10(n):
    s = 0
    i = 0
    while n > 0:
        s += (n % 5)*(5 ** i)
        n /= 10
        i += 1
    return s


def from_custom_base5(s):
    if not isinstance(s,str):
        raise TypeError("Input is not a String")
    if s == "":
        raise ValueError("empty string")
    conv1 = [chr(65+i) for i in range(5)]
    conv2 = [chr(97+i) for i in range(5)]
    num = 0
    for i in s:
        if i in conv1:
            num = num * 10 + conv1.index(i)
        elif i in conv2:
            num = num * 10 + conv2.index(i)
        else:
            raise ValueError
    return base5_to_10(num)



# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ca" == to_custom_base5(10)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ca")