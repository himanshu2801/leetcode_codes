"""
Question...
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Solution...
"""
class Solution:
    def convertToBase7(self, n: int) -> str:
        if n>0:
            i=1
            s=0
            while(n!=0):
                r=n%7
                n=n//7
                s=s+(r*i)
                i=i*10
            return(str(s))
        elif n==0:
            return("0")
        else:
            n=-1*n
            i=1
            s=0
            while(n!=0):
                r=n%7
                n=n//7
                s=s+(r*i)
                i=i*10
            return("-"+str(s))  
