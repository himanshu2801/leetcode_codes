"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
Accepted
33,754
Submissions
56,201
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        i=0
        while i<len(arr):
            if arr.count(arr[i])>=len(arr)//4+1:
                return arr[i]
            else:
                i = i + arr.count(arr[i])
        return -1
