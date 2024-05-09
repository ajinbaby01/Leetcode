#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (55.66%)
# Likes:    10176
# Dislikes: 1411
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def __init__(self):
        self.visited = set()

    def isHappy(self, n: int) -> bool:
        # return self.recursive(n)
        return self.iterative(n)

    def iterative(self, n: int) -> bool:
        visited = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in visited:
                return False
            visited.add(n)
        return True

    def recursive(self, n: int) -> bool:
        if n == 1:
            return True

        if n in self.visited:
            return False
        self.visited.add(n)

        summed = 0
        while n > 0:
            summed += (n % 10) ** 2
            n //= 10
        return self.recursive(summed)

# @lc code=end
