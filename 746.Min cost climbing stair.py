"""
Question...
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Solution...
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        pprev, prev, n = 0, 0, len(cost)
        for i in range(2, n + 1): 
            c = min(pprev + cost[i - 2], prev + cost[i - 1])
            pprev, prev = prev, c
        return prev
