"""
Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        count=0
        if len(nums)==0:
            return 1
        if len(nums)==1:
            if nums[0]==1:
                return 2
            else:
                return 1
        for i in nums:
            if i<=0:
                count+=1
        j=1
        for i in range(count,len(nums)):
            if nums[i]==j:
                j+=1
            else:
                return j
        return j
        
