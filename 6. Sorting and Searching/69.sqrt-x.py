#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.26%)
# Likes:    8008
# Dislikes: 4468
# Total Accepted:    1.9M
# Total Submissions: 5M
# Testcase Example:  '4'
#
# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down
# to the nearest integer, 2 is returned.
#
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # return self.babylonian(x)
        return self.binary_search(x)

    def binary_search(self, x: int) -> int:
    # Only works since we need to find the nearest integer and not the exact square root
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            # mid = (left + right) / 2 Will result in overflow for large numbers of x
            mid = left + (right - left)//2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right

    def babylonian(self, x: int, precision=0.01) -> int:
        # Find the exact square root (Remove floor())
        if x == 0:
            return 0

        guess = x / 2
        while True:
            new_guess = (guess + x / guess) / 2
            if abs(new_guess - guess) < precision:
                return floor(new_guess)
            guess = new_guess
# @lc code=end
