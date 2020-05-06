# leetcode_codes
Here you access all ofmy code that i solved on leet code
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution...


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if x not in lst:
                lst.append(nums[i])
            else:
                return  [nums.index(x),i]
