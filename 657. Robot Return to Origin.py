"""
Question...
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
Solution...
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r,l,u,d=0,0,0,0
        for i in range(len(moves)):
            if moves[i]=='R':
                r=r+1
                l=l-1
            elif moves[i]=='L':
                l=l+1
                r=r-1
            elif moves[i]=='U':
                u=u+1
                d=d-1
            else:
                d=d+1
                u=u-1
        if r==0 and u==0 and l==0 and d==0:
            return True
        else:
            return False
        
