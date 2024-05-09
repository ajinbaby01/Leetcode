#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (46.53%)
# Likes:    6730
# Dislikes: 426
# Total Accepted:    1.3M
# Total Submissions: 2.7M
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
#
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
#
#
# Example 2:
#
#
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
#
#
# Example 3:
#
#
# Input: n = 3
# Output: false
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.logarithmic(n)
        # return self.bitManipulation(n)

    def logarithmic(self, n: int) -> bool:
        if n <= 0:
            return False
        while True:
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n //= 2
    # Time: O(logn), Space: O(1)

    def bitManipulation(self, n: int) -> bool:
        return n > 0 and (n & n - 1) == 0

    # Time: O(1), Space: O(1)


# @lc code=end
