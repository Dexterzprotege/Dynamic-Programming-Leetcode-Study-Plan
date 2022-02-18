# Questions: https://leetcode.com/problems/house-robber-ii/submissions/

# Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robhouses(arr):
            n = len(arr)
            if not arr:
                return 0
            if n == 1:
                return arr[0]
            dp = [0]*n
            dp[0] = arr[0]
            dp[1] = max(dp[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+arr[i], arr[i], dp[i-1])
            return dp[-1]
        
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        return max(robhouses(nums[:len(nums)-1]), robhouses(nums[1:]))
      
# Verdict:
# Runtime: 58 ms, faster than 19.60% of Python3 online submissions for House Robber II.
# Memory Usage: 13.9 MB, less than 91.88% of Python3 online submissions for House Robber II.
