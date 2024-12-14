#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

import math


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s: str) -> str:
    """
    Returns the s string with the 'ing' string concatenated to it,
    If the s string ends in 'ing', the concatenated string will be 'ly' instead.
    If the length of s is shorter than 3, the function will return s.

    Args:
        s (str): Received string.

    Returns:
        str: The resulting string.
    """

    # If s is shorter than 3 chars return s.
    if len(s) < 3:
        return s

    # Save the last three chars of s.
    str_tail = s[-3:]

    # Add 'ing' to the end of s, unless it already ends in 'ing', in that case add 'ly' to the end of s.
    if str_tail != 'ing':
        result = s + 'ing'
    else:
        result = s + 'ly'

    # Return the result string.
    return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s: str) -> str:
    """
    If the s string contains a 'not...bad' expression,
    this function will replace it with 'good'.
    Example: 'This dinner is not that bad!' yields: 'This dinner is good!'.

    Args:
        s (str): Received string.

    Returns:
        str: The resulting string.
    """

    # Find the index of the first appearance of the 'not' and 'bad' substrings in s.
    index_of_not = s.find('not')
    index_of_bad = s.find('bad')

    # Declare the result string to be equal to s.
    result_str = s

    # If both substrings exist in s, and 'not' comes before 'bad', replace the expression with 'good'.
    if index_of_not < index_of_bad and index_of_not != -1:
        slice_to_replace = s[index_of_not:index_of_bad + len('bad')]
        result_str = s.replace(slice_to_replace, 'good')

    # return the resulting string.
    return result_str


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a: str, b: str) -> str:
    """
    Receives two strings and splits them in half.
    Returns a string made of the interpolated halves of both strings:
    a-front + b-front + a-back + b-back.

    Args:
        a (str): Received string #1.
        b (str): Received string #2.

    Returns:
        str: The resulting string.
    """

    # Find the middle point of each string (Rounded up)
    a_middle_point = math.ceil(len(a)/2)
    b_middle_point = math.ceil(len(b)/2)

    # Create a string made of the interpolated halves of both strings:
    # a-front + b-front + a-back + b-back.
    resulting_str = a[:a_middle_point] + b[:b_middle_point] + a[a_middle_point:] + b[b_middle_point:]

    # return the resulting string.
    return resulting_str


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
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


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
