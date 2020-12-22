"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = 0
        p2 = len(nums)-1
        p1 = 0
        while p1<=p2:
            if nums[p1] == 2:
                nums[p2],nums[p1] = nums[p1],nums[p2]
                p2 -= 1
            elif nums[p1] == 0:
                nums[p0],nums[p1] = nums[p1],nums[p0]
                p0 += 1
                p1 += 1
            else:
                p1 += 1
        return nums
        
