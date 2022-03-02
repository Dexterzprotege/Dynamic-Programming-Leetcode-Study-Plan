# Question: https://leetcode.com/problems/maximum-sum-circular-subarray/

# Solution:
class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        # 1. Find maximum subarray sum using kadane's algorithm (max) 
        # 2. Find minimum subarray sum using kadane's algorithm (min)
        # 3. Find total sum of the array (sum)
        # 4. Now, if sum == min return max
        # 5. Otherwise, return maximum ( max, sum - min )
        
        maxHere, maxSoFar = arr[0], arr[0]
        minHere, minSoFar = arr[0], arr[0]
        summ = arr[0]
        for i in range(1, len(arr)):
            maxHere = max(arr[i], maxHere + arr[i])
            maxSoFar = max(maxSoFar, maxHere)

            minHere = min(arr[i], minHere + arr[i])
            minSoFar = min(minSoFar, minHere)
            
            summ += arr[i]
        
        maxSubArraySum, minSubArraySum = maxSoFar, minSoFar
        
        # If Sum and MinSubarray are same, their difference would be 0, and hence returning maxSubArray
        if summ == minSubArraySum:
            return maxSubArraySum
        return max(maxSubArraySum, summ-minSubArraySum)
      
# Verdict:
# Runtime: 1225 ms, faster than 5.05% of Python3 online submissions for Maximum Sum Circular Subarray.
# Memory Usage: 18.9 MB, less than 46.44% of Python3 online submissions for Maximum Sum Circular Subarray.
