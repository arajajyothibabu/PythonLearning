__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit4_assignment_01
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit4utils
import string

def list_out_words(input):
    result = []
    f = open(input)
    for line in f:
        if len(line.strip()) != 0 and line.strip()[0] != '#':
            result.append(line.strip())
    result.sort(key=str.lower)
    return result


def is_anagram(s1, s2):
    return sorted(list(s1.lower())) == sorted(list(s2.lower()))


def lowered(input):
    if len(input) == 1:
        return input[0].lower()


def find_anagrams(input):
    lines = []
    list1 = []
    i = 0
    while i < len(input):
        list1.append(input[i])
        j = i + 1
        while j < len(input):
            if is_anagram(input[i], input[j]):
                list1.append(input[j])
                input.remove(input[j])
                j -= 1
            j += 1
        input.remove(input[i])
        lines.append(list1)
        list1 = []
    lines.sort(key=lowered)
    return sorted(lines, key=len, reverse=True)


def anagram_sort(source, destination):
    output = find_anagrams(list_out_words(source))
    d = open(destination,'wb')
    for line in output:
        line.sort(key=str.lower)
        for x in line:
            d.write(x + "\n")


def test_anagram_sort():
    source = unit4utils.get_input_file("unit4_testinput_02.txt")
    expected = unit4utils.get_input_file("unit4_expectedoutput_02.txt")
    destination = unit4utils.get_temp_file("unit4_output_02.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
