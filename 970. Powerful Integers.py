"""
Question...
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Solution...
"""
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        lst=[]
        for i in range(20):
            for j in range(20):
                temp=x**i+y**j
                if temp<=bound:
                    lst.append(temp)
                else:
                    break
        return list(set(lst))
       
