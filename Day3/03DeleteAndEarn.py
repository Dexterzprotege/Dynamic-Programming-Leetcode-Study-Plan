# Question: https://leetcode.com/problems/delete-and-earn/

# ----------------------------------------------------------------------------------------- #

# Solution: 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        numset = sorted(list(set(nums)))
        curr1, curr2 = 0, 0
        for i in range(len(numset)):
            currVal = numset[i]*dic[numset[i]]
            if i > 0 and numset[i] - 1 == numset[i-1]:
                curr1, curr2 = curr2, max(currVal + curr1, curr2)
            else:
                curr1, curr2 = curr2, currVal + curr2
        return curr2
      
# Verdict:
# Runtime: 95 ms, faster than 39.58% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.1 MB, less than 88.36% of Python3 online submissions for Delete and Earn.

# ----------------------------------------------------------------------------------------- #
  
# Solution: Dynamic Programming
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        # Count the frequency
        for i in nums:
            dic[i] += 1
        # Make sure to remove duplicates
        numset = sorted(list(set(nums)))
        dp = [0] * len(numset)
        
        # First value is the count*frequency of first element
        dp[0] = numset[0]*dic[numset[0]]
        for i in range(1, len(numset)):
            # If the current number is adjacent to we can consider only three things:
              # 1. Current count*frequency
              # 2. Previous DP value
              # 3. Current cout*frequency + dp[i-2]
            if numset[i] - 1 == numset[i-1]:
                dp[i] = max(dp[i-1], numset[i]*dic[numset[i]], numset[i]*dic[numset[i]]+dp[i-2])
            # Else we can just consider previous element
            else:
                dp[i] = dp[i-1] + numset[i]*dic[numset[i]]
        return dp[-1]
      
# Verdict:
# Runtime: 60 ms, faster than 81.25% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.2 MB, less than 88.36% of Python3 online submissions for Delete and Earn.

# ----------------------------------------------------------------------------------------- #
