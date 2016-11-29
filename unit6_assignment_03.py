__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first == None or second == None:
        return False
    if len(first) != len(second):
        return False
    f = list(first.lower())
    s = list(second.lower())
    f.sort()
    s.sort()
    if f == s:
        return True
    else:
        return False


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True == are_anagrams("ArAjA", "araja")
    assert False == are_anagrams("AraJA", "ARAJAJB")
    assert True == are_anagrams("hai123", "123HAI")
    assert True == are_anagrams("", "")
    assert True == are_anagrams("pit  ", "  pit")
    assert False == are_anagrams(None, None)
    assert False == are_anagrams("bigg", "biig")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_are_anagrams(are_anagrams)
