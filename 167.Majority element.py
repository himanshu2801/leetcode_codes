"""
Question...
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Solution...
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        i=0
        while(i<=l//2):
            x=nums.count(nums[i])
            if x>l//2:
                return nums[i]
            i=i+x
