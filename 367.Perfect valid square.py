"""
Question...
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Solution...
"""
import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**0.5)-math.floor(num**0.5)==0:
            return True
        else:
            return False
