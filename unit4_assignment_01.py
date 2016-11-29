__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
3. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
'''

import unit4utils

def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    lines = []
    f = open(source)
    d = open(destination,'wb')
    for line in f:
        if len(line.strip()) != 0 and line.strip()[0] != '#':
            lines.append(line.strip().lower())
    lines.sort()
    for line in lines:
        d.write(line + "\n")


def test_sort_words():
    source = unit4utils.get_input_file("unit4_testinput_01.txt")
    expected = unit4utils.get_input_file("unit4_expectedoutput_01.txt")
    destination = unit4utils.get_temp_file("unit4_output_01.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
