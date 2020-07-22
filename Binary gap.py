"""
Question...
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Solution...
"""
class Solution:
    def binaryGap(self, N: int) -> int:
        s=bin(N)
        s=s[2:]
        if s.count('1')==1:
            return 0
        max=0
        lst=[]
        for i in range(len(s)):
            if s[i]=='1':
                lst.append(i)
        for i in range(len(lst)-1):
            if max<lst[i+1]-lst[i]:
                max=lst[i+1]-lst[i]
        return max
            
