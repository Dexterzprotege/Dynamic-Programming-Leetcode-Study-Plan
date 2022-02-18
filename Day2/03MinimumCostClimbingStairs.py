# Question: https://leetcode.com/problems/min-cost-climbing-stairs/

# Solution:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        for i in range(2, len(cost)):
            temp = cost[i] + min(first, second)
            first = second
            second = temp
        return min(first, second)
      
# Verdict:
# Runtime: 78 ms, faster than 51.07% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 13.9 MB, less than 99.34% of Python3 online submissions for Min Cost Climbing Stairs.
