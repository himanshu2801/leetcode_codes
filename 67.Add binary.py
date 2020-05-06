"""
Question...

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Solution...

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)+int(b,2)
        return bin(x)[2:]
