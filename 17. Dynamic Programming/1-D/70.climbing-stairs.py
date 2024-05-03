#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (52.27%)
# Likes:    21613
# Dislikes: 805
# Total Accepted:    3.2M
# Total Submissions: 6.1M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Can also be solved with two variables like Fibonacci
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [None] * n
        memo[0] = 1
        memo[1] = 2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n - 1]
# @lc code=end
