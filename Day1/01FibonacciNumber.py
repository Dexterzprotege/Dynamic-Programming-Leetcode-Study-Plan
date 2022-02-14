# Question: https://leetcode.com/problems/fibonacci-number/

# Solution:
class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        for i in range(31):
            fib.append(fib[-1]+fib[-2])
        return fib[n]
      
# Verdict:
# Runtime: 52 ms, faster than 42.22% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 74.25% of Python3 online submissions for Fibonacci Number.
