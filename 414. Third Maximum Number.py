"""
Question...
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Solution...
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        if len(nums)<3:
            return max(nums)
        else:
            nums=sorted(nums,reverse=True)
            return nums[2]
