"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d,ans={},""
        l=str.split(" ")
        if len(pattern)!=len(l):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d and l[i] not in d.values():
                d[pattern[i]]=l[i]
        for i in pattern:
            if i in d:
                ans+=d[i]+" "
        return ans.strip()==str
        
