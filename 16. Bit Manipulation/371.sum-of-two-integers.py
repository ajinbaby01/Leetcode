#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (51.39%)
# Likes:    4113
# Dislikes: 5463
# Total Accepted:    474.4K
# Total Submissions: 915.1K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
#
#
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
#
# -1000 <= a, b <= 1000
#
#
#

# @lc code=start
class Solution:
    # Read explanation on notion
    def getSum(self, a: int, b: int) -> int:
        # while b != 0:
        #     carry = (a & b) << 1
        #     a = a ^ b
        #     b = carry
        # return a

        # In python, overflows can occur since bits are represented using more than 32 bits
        # Hence masking is required : https://leetcode.com/problems/sum-of-two-integers/solutions/489210/read-this-if-you-want-to-learn-about-masks/

        mask = 0xffffffff # 32bit mask
        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
# @lc code=end
