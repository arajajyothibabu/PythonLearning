__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).
'''

def left_binary_search(input, value):
    low = 0
    high = len(input)-1
    while low <= high:
        mid = (low + high)/2
        if input[mid] == value:
            x = mid-1
            while x >= 0:
                if input[x] == value:
                    mid -= 1
                x -= 1
            return mid
        elif input[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 2 == left_binary_search([1,2,3,3,4,4,5], 3)
    assert 0 == left_binary_search([2,2,2,2,2], 2)
    assert 6 == left_binary_search([1,2,3,3,4,4,5], 5)
    assert 0 == left_binary_search([1,2,3,3,4,4,5], 1)
    assert 4 == left_binary_search([1,2,3,3,4,4,5], 4)
    assert 4 == left_binary_search(range(10), 4)
    assert -1 == left_binary_search(range(10), -10)


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_left_binary_search(left_binary_search)
