Question

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Solution...
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=nums.count(target)
        if x==0:
            return [-1,-1]
        else:
            temp=nums.index(target)
            nums.reverse()
            temp1=nums.index(target)
            return [temp,len(nums)-temp1-1]
