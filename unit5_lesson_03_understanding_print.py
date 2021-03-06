__author__ = 'Kalyan'

print_debugging = '''
As the name suggests, you add additional print statements as required into the buggy function to be clear about what
intermediate states when the test fail. You need to figure out what additional state you want to see etc.

Then you infer what went wrong based on the print output.
'''

# This function takes 2 or more sequences and returns the length of sequence
# of smallest length. Fix the bug by adding appropriate print statements

def min_length(seq1, seq2, *more_seqs):
    print "Input", more_seqs
    if more_seqs:
        x = len(more_seqs[0])
        for seq in more_seqs:
            if x > len(seq):
                x = len(seq)
        return min(len(seq1), len(seq2), x)
    else:
        return min(len(seq1), len(seq2))


def test_min_length():
    assert 4 == min_length("hell", "hello")
    assert 1 == min_length(range(3), "a", "what")
    assert 2 == min_length(range(3), "apple", "so", "what")
    assert 2 == min_length(range(3), "apple", "so")



# Fix this function only so that add_new_email works as expected.
def buggy_contains(current, new):
    for mail in current:
        i = 0
        result = []
        c = 0
        while i < len(mail):
            if mail[i] == new[i] or abs(ord(mail[i])-ord(new[i])) == 32:
                c += 1
            i += 1
        if c == len(mail):
                return True

    return False


# Given a list of emails(current) and a new email (new),
# add the new email to existing list if it does not exist.
def add_new_mail(existing, new):
    if buggy_contains(existing, new):
        return # already exists nothing to do.
    existing.append(new)

# See the failing assert and add appropriate prints in function above which will help you debug
def test_add_new_mail():
    mails = []
    add_new_mail(mails, "a@b.com")
    assert 1 == len(mails)

    # add with a different case, should be considered same as a@b.com
    add_new_mail(mails, "A@b.com")
    assert 1 == len(mails)

    add_new_mail(mails, "C@b.com")
    assert 2 == len(mails)

    # same as C@b.com
    add_new_mail(mails, "c@b.com")
    assert 2 == len(mails)

    # same as C@b.com
    add_new_mail(mails, "C@b.com")
    assert 2 == len(mails)
