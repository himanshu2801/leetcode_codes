"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        lst, result = [], []
        n =len(candidates)
        def backtrack(candidates, lst, result, index, target, n):
            if target == 0:
                result.append(lst[:])
            if target < 0:
                return
            prev=-1
            for i in range(index,n):
                if prev!=candidates[i]:
                    lst.append(candidates[i])
                    backtrack(candidates, lst, result, i+1, target-candidates[i], n)
                    lst.pop()
                    prev = candidates[i]
        backtrack(candidates, lst, result, 0, target, n)
        return result
