__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Given a sentence transform all words in it according to
the following guidelines:

1. Move all vowels before all the consonents
2. Maintain relative ordering among the vowels and consonents.
3. If two equal letters come next to each other (case insensitive duplicates), drop the second letter
4. Preserve the case of the original letters.
5. Words are separated by spaces. Drop all non-letters like digits and punctuation and special chars in the sentence.

For e.g eagle becomes eaegl, ApPle become Aepl(repeating P dropped)

Write helper sub routines as required
'''
# do type checking, non-str should raise TypeException


def into_words(sentence):
    words = []
    k = 0
    i = 0
    while i < len(sentence):
        if sentence[i] == ' ' or sentence[i] == ',' or sentence[i] == '.':
            word = sentence[k:i]
            k = i+1
            words.append(word.strip())
        if i+1 < len(sentence):
            if sentence[i] == ',':
                i += 1
        i += 1

    words.append(sentence[k:])
    return words


def is_vowel(c):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    if c in vowels:
        return True
    return False

def unique_word(word):
    for i in word:
        x = ord(i)
        if x<65 or (x >90 and x < 97) or x > 122:
            word.remove(i)
        if i.isdigit():
            word.remove(i)
    i = 0
    while i+1 < len(word):
        x = ord(word[i])
        y = ord(word[i+1])
        if x == y or x+32 == y or x-32 == y or x == y+32 or x == y-32:
            word.remove(word[i+1])
        i += 1
    return word


def transform(sentence):
    words = into_words(sentence)
    final = []
    for word in words:
        l = unique_word(list(word))
        print l
        l1 = []
        i = 0
        while i < len(l):
            if is_vowel(l[i]):
                l1.append(l[i])
                l.remove(l[i])
            else:
                i += 1
        print l
        for j in l:
            l1.append(j)
        final.append(l1)
    result = []
    for x in final:
        result.append("".join(x))
    print " ".join(result)
    return " ".join(result)


def test_transform():
    assert "Aepl eaegl and ES" == transform("Apple, eagle and SE00e")