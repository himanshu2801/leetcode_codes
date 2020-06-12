"""
question...
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
Solution...
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x)[2:]
        l=0
        y=bin(y)[2:]
        if len(x)==len(y):
            pass
        else:
            if len(x)>len(y):
                y="0"*(len(x)-len(y)) + y
            else:
                x="0"*(len(y)-len(x)) + x
        for i in range(len(x)):
            if x[i]!=y[i]:
                l=l+1
            else:
                pass
        return l
        
