# Description: This file contains code for the palindrome function with a known fault at line 3.
# fault: string reversed from the second index from the right side rather than the first.
def is_palindrome(s):
    reversed_s = s[::-2]  # fault is here replaced 1 by 2

    if reversed_s == s:
        return True
    else:
        return False
