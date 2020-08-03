"""
Question...
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Solution...
"""
class Solution {
    public int findDuplicate(int[] nums) {
        
        for(int i=0;i<nums.length;i++){
            for(int j=i;j<nums.length;j++){
                if (nums[i]-nums[j]==0 && i!=j){
                    return nums[i];
                }
            }
        }
        return 0;
    }
}
"""
Python version 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                return i
        """
