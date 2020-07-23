"""
Question...
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
Solution...
"""
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A=list(A.split(" "))
        B=list(B.split(" "))
        lst=[]
        for i in range(len(A)):
            if A.count(A[i])==1 and A[i] not in B:
                lst.append(A[i])
        for i in range(len(B)):
            if B.count(B[i])==1 and B[i] not in A:
                lst.append(B[i])
        return lst
                
        
