# Question: https://leetcode.com/problems/climbing-stairs/

# ----------------------------------------------------------------------------------------- #

# Solution 4: Top Down Memoization: O(N) + O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, dp):
            if dp[n] < 0:
                dp[n] = helper(n-1, dp) + helper(n-2, dp)
            return dp[n]
        if n == 1:
            return 1
        dp = [-1] * n
        dp[0], dp[1] = 1, 2
        return helper(n-1, dp)
      
# Verdict:
# Runtime: 51 ms, faster than 23.60% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14 MB, less than 64.57% of Python3 online submissions for Climbing Stairs.

# ----------------------------------------------------------------------------------------- #

# Solution 3: DP Bottom Up Constant space O(N) + O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
        return b

# Verdict:
# Runtime: 64 ms, faster than 5.22% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 89.20% of Python3 online submissions for Climbing Stairs.

# ----------------------------------------------------------------------------------------- #

# Solution 2: DP Bottom Up O(N) + O(N)
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
      
# Verdict:
# Runtime: 56 ms, faster than 14.01% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 89.20% of Python3 online submissions for Climbing Stairs.

# ----------------------------------------------------------------------------------------- #

# Solution 1: Recursive Top Down Apptoach O(2^n)
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Verdict:
# TLE w/o @lru_cache
# Runtime: 36 ms, faster than 56.60% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 89.20% of Python3 online submissions for Climbing Stairs.

# ----------------------------------------------------------------------------------------- #
