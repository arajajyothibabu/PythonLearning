__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''
def rotate_right(input):
    return input[-1:] + input[:-1]

def get_right_rotations(str1, str2):
    if (str1 == None and str2 == None) or (str1 == "" and str2 == ""):
        return 0
    elif str1 == None or str2 == None or len(str1) != len(str2):
        return -1
    else:
        i = 0
        while i < len(str1):
            str1 = rotate_right(str1)
            if str1 == str2:
                return i+1
            i += 1
        return -1



# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")
    assert 2 == get_right_rotations("abcd", "cdab")
    assert -1 == get_right_rotations("", "dabc")
    assert -1 == get_right_rotations("bcdef", "dabc")