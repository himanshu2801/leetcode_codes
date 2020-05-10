"""
Question...
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Solution...
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        A=list(A)
        B=list(B)
        if len(A)!=len(B):
            return False
        if len(A)==0:
            return True
        for i in range(len(A)):
            temp=A[0]
            for j in range(len(A)-1):
                A[j]=A[j+1]
            A[len(A)-1]=temp
            if A==B:
                return True
        return False
            
        
