"""
Question...
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Solution...
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        """s=" ".join(s.split())
        l=0
        lst=[]
        for i in range(len(s)):
            if s[i]==" ":
                lst.append(s[l:i])
                l=i+1
        lst.append(s[l:])
        lst.reverse()
        s=" ".join(lst)
        return s"""
                  or
        return " ".join(s.split()[::-1])
        
