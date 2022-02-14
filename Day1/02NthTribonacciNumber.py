# Question: https://leetcode.com/problems/n-th-tribonacci-number/

# ----------------------------------------------------------------------------------------------- #

# Solution 2:
class Solution:
    def tribonacci(self, n):
        a, b, c = 1, 0, 0
        for i in range(n): 
            a, b, c = b, c, a + b + c
        return c

# Verdict:
# Runtime: 58 ms, faster than 10.65% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 75.69% of Python3 online submissions for N-th Tribonacci Number.

# ----------------------------------------------------------------------------------------------- #

# Solution 1:
class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]
        for i in range(3, 38):
            fib.append(fib[-1]+fib[-2]+fib[-3])
        return fib[n]

# Verdict:
# Runtime: 40 ms, faster than 48.83% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 75.69% of Python3 online submissions for N-th Tribonacci Number.

# ----------------------------------------------------------------------------------------------- #
