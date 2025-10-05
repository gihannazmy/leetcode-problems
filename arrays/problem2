
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 +str1:
            return ''
        res = str1[:math.gcd(len(str1), len(str2))]


        return res
    

# the main idea here is using gcd func
# math.gcd(x, y)
# Parameters: x, y is Two non-negative integers (at least one of them must be non-zero).

# Returns:

#     The greatest common divisor of x and y.
#     If either x or y is 0, the result is the absolute value of the non-zero number.
# Examples of using math.gcd() function

# Example 1: GCD of a number and 0
# Loading Playground...

import math

print(math.gcd(0, 25))


Output :25

