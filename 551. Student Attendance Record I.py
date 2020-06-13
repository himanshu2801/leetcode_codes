"""
Question...
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
Solution...
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1:
            return False
        l=0
        for i in range(len(s)-1):
            if s[i]=='L' and s[i+1]=='L':
                l=l+1
            else:
                l=0
            if l==2:
                return False
        return True
            
        
