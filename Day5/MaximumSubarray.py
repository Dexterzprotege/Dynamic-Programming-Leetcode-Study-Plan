# Question: https://leetcode.com/problems/maximum-subarray/

# Solution:
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxHere, maxSoFar = arr[0], arr[0]
        for i in range(1, len(arr)):
            maxHere = max(arr[i], maxHere + arr[i])
            maxSoFar = max(maxSoFar, maxHere)
        return maxSoFar
        
# Verdict:
# Runtime: 907 ms, faster than 61.12% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.6 MB, less than 30.74% of Python3 online submissions for Maximum Subarray.
