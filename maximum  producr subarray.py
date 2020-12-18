"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min1 = nums[0]
        result = nums[0]
        max1 = nums[0]
        current = nums[0]
        for i in range(1,len(nums)):
            current = max(max1*nums[i], min1*nums[i], nums[i])
            current_min = min(max1*nums[i], min1*nums[i], nums[i])
            result = max(current, result)
            max1 = current
            min1 = current_min
        return result
            
        
