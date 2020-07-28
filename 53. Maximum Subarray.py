"""
Question...
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
Solution...
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1=0
        temp=0
        for i in range(len(nums)):
            temp=temp+nums[i]
            if temp>0:
                if temp>max1:
                    max1=temp
            else:
                temp=0
        if temp==0 and max(nums)<0:
            temp=max(nums)
            return temp
        else:
            return max1
        
        
