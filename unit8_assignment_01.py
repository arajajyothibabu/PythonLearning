__author__ = 'Kalyan'

problem = """
 We are going to revisit unit4 assignment2 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
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
    d = open(destination,'w')
    for line in output:
        line.sort(key=str.lower)
        for x in line:
            d.write(x + '\n')


def call_anagram_sort():
    anagram_sort(sys.argv[1], "unit8_assignment_01_result.txt")

if __name__ == "__main__":
    call_anagram_sort()
    #sys.exit(main())