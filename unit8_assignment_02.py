__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

def pig_latin(word):
    if ord(word[0]) > 64:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        punc_flag = False
        if word[-1:] == "," or word[-1:] == ".":
            punc_flag = True
            lis = list(word[:-1])
            if word[-1:] == ",":
                char = ','
            else:
                char = '.'
        else:
            lis = list(word)
        flag = False
        while lis[0] not in vowels:
            if ord(lis[0]) < 98:
                flag = True
            lis.append(lis[0])
            lis.remove(lis[0])
        lis.append("ay")
        if punc_flag:
            lis.append(char)
        if flag:
            lis[0] = chr(ord(lis[0]) - 32)
        return "".join(lis)
    return word


def read_input():
    while True:
        inputs = input("Enter String:").split(' ')
        output = ""
        for word in inputs:
            output += (pig_latin(word) + " ")
        write_output(output.strip())


def write_output(output):
    print output


def game():
    read_input()

if __name__ == "__main__":
    game()
    #sys.exit(main())