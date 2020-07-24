"""
Question...
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Solution...
"""
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A=sorted(A)
        i=0;
        n=len(A)
        while i<n:
            temp=A.count(A[i])
            if temp==n//2:
                return A[i]
            i=i+A.count(A[i])
        
