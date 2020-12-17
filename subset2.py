"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lst = []
        subset = []
        def backtrack(lst, subset, nums, index):
            if len(lst)<=len(nums) and lst not in subset:
                subset.append(lst[:])
            else:
                return
            for i in range(index, len(nums)):
                lst.append(nums[i])
                backtrack(lst, subset,nums, i+1)
                lst.pop()
        backtrack(lst, subset, nums, 0)
        return subset
        
