"""
Question...
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
Solution...
"""
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x,y,z=points
        x1,x2=x
        y1,y2=y
        z1,z2=z
        if x==y or y==c or x==z:
            return False
        else:
            return (x1-y1)*(x2-z2)!=(x1-z1)*(x2-y2)
