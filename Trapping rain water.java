"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
 """
 class Solution {
    public int trap(int[] height) {
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();
        if(height.length==0){
            return 0;
        }
        int max = height[0];
        for(int i=0;i<height.length;i++){
            if (max < height[i]){
                max = height[i];
            }
            left.add(max);
        }
        max = height[height.length - 1];
        for(int i=height.length - 1;i>-1;i--){
            if (max < height[i]){
                max = height[i];
            }
            right.add(max);
        }
        int sum = 0;
        for(int i=0;i<height.length;i++){
            int temp = Math.min(left.get(i),right.get(height.length-1-i)) - height[i];
            if(temp>0){
                sum = sum + temp;
            }
        }
        return sum;
    }
}
