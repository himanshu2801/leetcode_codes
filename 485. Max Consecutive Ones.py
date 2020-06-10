"""
Question...
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Solution...
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        l=0
        for i in nums:
            if i==1:
                l=l+1
            else:
                l=0
            if l>max:
                max=l
        return max
            
        
