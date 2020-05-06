"""
Question...
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Solution...
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lst=[]
        l=len(nums)
        nums.sort()
        i=0
        while(i!=l):
            x=nums.count(nums[i])
            if x>l//3:
                lst.append(nums[i])
            i=i+x
        return lst
        
