"""
Question...
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Solution...
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        lst=[0]*len(A)
        t_e,t_o=0,1
        for i in range(len(A)):
            if ((i%2==0 and A[i]%2==0) or (i%2!=0 and A[i]%2==0)):
                lst[t_e]=lst[t_e]+A[i]
                t_e=t_e+2
            else:
                lst[t_o]=lst[t_o]+A[i]
                t_o=t_o+2
        return lst
            
        
