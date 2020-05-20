"""
Question...
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Solution...
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            
            if nums[i]>nums[i+1]:
                return i
            i=i+1
        return len(nums)-1
        
