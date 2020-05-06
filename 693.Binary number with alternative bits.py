"""
Question...
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Solution...
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=bin(n)
        if "00" in x or "11" in x:
            return False
        else:
            return True
