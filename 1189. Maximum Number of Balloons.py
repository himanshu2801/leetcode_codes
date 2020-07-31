"""
Question...
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
Solution...
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a={'a':0,'b':0,'n':0,'l':0,'o':0}
        for i in text:
            if i=='b' or i=='a' or i=='n':
                a[i]=text.count(i)
            elif i=='l' or i=='o':
                a[i]=text.count(i)//2
            else:
                continue
        return min(a.values())
                
            
        
        
