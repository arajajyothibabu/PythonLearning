__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.

2. Feel free to create new helper functions if needed. Give good names though :)

3. Use builtins (sort, etc.) and datatypes that we have already seen so far (lists, dicts, sets etc.)
   instead of writing your own.

4. If something about the function spec is not clear, use the corresponding test
   for clarification

5. Note that the tests are not exhaustive, so do your own testing as well.

6. Don't use collections module to solve this problem, write your own code :).

7. Try to analyze the performance of your code - are you creating any unnecessary intermediate lists, or datatype
   coversions  calling sort more often than you need to etc.
'''


# return the top n most frequently occurring chars and their respective counts
# e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
# in case of a tie, return char which comes earlier in alphabet ordering
# e.g. cdbba,2 -> [(b,2) (a,1)]
# use standard types we have seen so far and builtin functions

import string

def top_chars(word, n):
    c = 0
    l1 = []
    l2 = list(set(word))
    for x in l2:
        l1.append(word.count(x))
    for x in range(len(l1)):
        for y in range(x+1, len(l1)):
            if l1[x] < l1[y] or (l1[x] == l1[y] and ord(l2[y]) < ord(l2[x])):
                z = l1[x]
                a = l2[x]
                l1[x] = l1[y]
                l2[x] = l2[y]
                l1[y] = z
                l2[y] = a
    l = zip(l2, l1)
    print l[0:]
    return l[:n]

def test_top_chars():
    assert [('p', 2)] == top_chars("app",1)
    assert [('p', 2), ('a',1)] == top_chars("app",2)
    assert [('p', 2), ('a',1)] == top_chars("app",3)

    assert [('x', 2)] == top_chars("xxcb", 1)
    assert [('a', 2), ('b', 1)] == top_chars("aacb", 2)
    assert [('a', 2), ('b', 1), ('c', 1)] == top_chars("aacb", 3)

    assert [('e', 3)] == top_chars("irreversible", 1)
    assert [('e', 3), ('r', 3)] == top_chars("irreversible", 2)
    assert [('e', 3), ('r', 3), ('i',2), ('b', 1)] == top_chars("irreversible", 4)
