__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by spaces. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    i = 0
    x = 0
    out = "";
    flag = 0
    while i < len(sentence):
        if i == 0 and sentence[i:i+6] == "either":
            return sentence
        if sentence[i] == " " and sentence[i+1:i+7] == "either" and x != 7 and sentence[i+7] == ' ':
            out += sentence[0:i+1]
            x = i+7
        if sentence[i] == " " and sentence[i+1:i+3] == "or" and sentence[i+3] == ' ':
            out += sentence[x+1:i]
            flag = 1
            break
        i += 1
    if out == "" or flag == 0 or x == 0:
        return sentence
    else:
        return out


def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "drink coffee" == prune_either_or("drink either coffee or tea")
    assert "we drink either of the two" == prune_either_or("we drink either of the two")
    assert "either come here or go there" == prune_either_or("either come here or go there")
    assert "" == prune_either_or("")
    assert "either or" == prune_either_or("either or")
    assert "either this or that" == prune_either_or("either this or that")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_prune_either_or(prune_either_or)
