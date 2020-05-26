"""
Question...
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
Solution...
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        temp=A[0]
        l,lst=0,[]
        for i in temp:
            for j in range(len(A)):
                if i in A[j]:
                    l=l+1
                    A[j]=A[j].replace(i,"",1)
            if l==len(A):
                lst.append(i)
            l=0
        return lst
            
            
            
        
