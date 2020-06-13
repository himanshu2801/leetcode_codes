"""
Question...
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Solution...
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        ans = 1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                ans+=i
                ans+=num//i
        return ans==num 
        
