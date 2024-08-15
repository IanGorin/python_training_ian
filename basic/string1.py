#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count: int) -> str:
    """
    Returns a string that states the exact amount of donuts.
    If the amount of donuts is equal or larger than 10,
    the string will state that the amount of donuts is: many

    Args:
        count (int): Number of donuts.

    Returns:
        str: A string that states the amount of donuts.
    """

    # Turn count into a string and save it as amount_of_donuts.
    amount_of_donuts = str(count)

    # If count is equal or greater than 10, save the amount of donuts as "many".
    if count >= 10:
        amount_of_donuts = 'many'

    # Format the output string with the chosen amount of donuts.
    result_str = f'Number of donuts: {amount_of_donuts}'

    # Return the output string.
    return result_str


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s: str) -> str:
    """
    Returns a string made of the first and last two characters of s.
    If the length of s is less than 2, Returns an empty string.

    Args:
        s (str): Received string.

    Returns:
        str: The resulting string.
    """

    # Assign an empty string to the result variable.
    result = ''

    # If s is equal or longer than 2 chars, result will be a string made of the first and last two chars of s.
    if len(s) >= 2:
        result = s[:2] + s[-2:]

    # Return the result string.
    return result


# C. fix_start
# Given a string s, return a string
# where all occurrences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s: str) -> str:
    """
    Returns a string where all instances of the first character (except for the first one)
    have been replaced with *.

    Args:
        s (str): Received string.

    Returns:
        str: The resulting string.
    """

    # Save the first char of s.
    first_char = s[0]

    # Save the rest of s.
    msg_tail = s[1:]

    # Save a version of msg_tail, in which every instance of first_char has been replaced with *.
    new_msg_tail = msg_tail.replace(first_char, '*')

    # Concatenate the first_char and new_msg_tail strings.
    result = first_char + new_msg_tail

    # Return the result string.
    return result


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a: str, b: str) -> str:
    """
    Returns a string made of the two received strings (separated by a whitespace),
    with their first two characters swapped between the strings.

    Args:
        a (str): Received string #1.
        b (str): Received string #2.

    Returns:
        str: The resulting string.
    """

    # Form a string from the first 2 chars of b and all the chars in a with an index of 2 or greater.
    str1 = b[:2] + a[2:]

    # Form a string from the first 2 chars of a and all the chars in b with an index of 2 or greater.
    str2 = a[:2] + b[2:]

    # Concatenate str1 and str2 separated by a whitespace.
    result = str1 + " " + str2

    # Return the result string.
    return result


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got: str, expected: str):
    """
    Checks if the got and expected strings are equal,
    Prints OK if they are, otherwise it prints X.

    Args:
        got (str): Result string from target function.
        expected (str): Expected result string for the given arguments.
    """

    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
