#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    function only returns True False on first letter
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    tests the literal lowercase 'c', always true.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    only catches last letter, flag variable reset each iteration.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    works - once flag is set true it stays true.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    stops execution on first False. Does the opposite of intended test.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1('Meep'))
    print(any_lowercase2('MEEP'))
    print(any_lowercase3('meeP'))
    print(any_lowercase4('mEeP'))
    print(any_lowercase5('meEp'))


if __name__ == '__main__':
    main()
