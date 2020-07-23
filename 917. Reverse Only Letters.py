"""
Question...
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Solution...
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        unknown="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1=""
        for i in range(len(s)):
            if s[i] in unknown:
                s1=s1+s[i]
        s1=s1[::-1]
        lst=list(s1)
        for i in range(len(s)):
            if s[i] not in unknown:
                lst.insert(i,s[i])
        return ''.join(lst)
        
        
        
