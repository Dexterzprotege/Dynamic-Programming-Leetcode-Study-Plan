# Question: https://leetcode.com/problems/house-robber/

# Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], nums[i], dp[i-1])
        return dp[-1]
      
# Verdict:
# Runtime: 32 ms, faster than 83.88% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 90.04% of Python3 online submissions for House Robber.
