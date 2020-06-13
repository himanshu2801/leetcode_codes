"""
Question...
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Soltion...
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s=["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","ZXCVBNMzxcvbnm"]
        lst=[]
        for i in range(len(words)):
            l=0
            if words[i][0] in s[0]:
                for j in words[i]:
                    if j not in s[0]:
                        l=1
                        break
            elif words[i][0] in s[1]:
                for j in words[i]:
                    if j not in s[1]:
                        l=1
                        break
            else:
                for j in words[i]:
                    if j not in s[2]:
                        l=1
                        break
            if l==0:
                lst.append(words[i])
        return lst
            
                
        
