# Question: https://leetcode.com/problems/jump-game-ii/

# Solution: BFS O(N2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, 0
        while right < len(nums)-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            res += 1
        return res
      
# Verdict:
# Runtime: 187 ms, faster than 66.88% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.1 MB, less than 50.63% of Python3 online submissions for Jump Game II.
