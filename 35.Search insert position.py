"""
Question...

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Solution...
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x=nums.count(target)
        if x==0:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            return nums.index(target)
        
