"""
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = list(set(nums))
        lst = []
        subset = []
        def backtrack(lst, subset, nums, index):
            if len(lst)<=len(nums):
                subset.append(lst[:])
            else:
                return
            for i in range(index, len(nums)):
                lst.append(nums[i])
                backtrack(lst, subset,nums, i+1)
                lst.pop()
        backtrack(lst, subset, nums, 0)
        return subset
        
