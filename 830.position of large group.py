"""
Question...
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Solution...
"""
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i,count,lst=0,0,[]
        while i!=len(s)-1:
            if s[i]==s[i+1]:
                count=count+1
                if ((count>=2 and i+1==len(s)-1) or (count>=2 and s[i+1]!=s[i+2])):
                    lst.append([i-count+1,i+1])
            else:
                count=0
            i=i+1   
        return lst
