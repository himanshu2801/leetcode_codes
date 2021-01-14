"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
"""
class Solution {
    public void nextPermutation(int[] nums) {
        int pointer = nums.length-2;
        while(pointer>=0 && nums[pointer]>=nums[pointer+1]){
            pointer--;
        }
        if(pointer==-1){
            reverseArray(0,nums.length-1,nums);
        }
        else{
        for(int i=nums.length-1;i>pointer;i--){
            if(nums[i]>nums[pointer]){
                int temp=nums[i];
                nums[i]=nums[pointer];
                nums[pointer]=temp;
                break;
            }
        }
        }
        if(pointer!=-1){
        reverseArray(pointer+1,nums.length-1,nums);}
    }
    void reverseArray(int i,int j,int[] nums){
        while(i<j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}
