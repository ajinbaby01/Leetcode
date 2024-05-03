#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
#
# https://leetcode.com/problems/number-of-even-and-odd-bits/description/
#
# algorithms
# Easy (71.56%)
# Likes:    264
# Dislikes: 104
# Total Accepted:    42.3K
# Total Submissions: 58.3K
# Testcase Example:  '17'
#
# You are given a positive integer n.
#
# Let even denote the number of even indices in the binary representation of n
# (0-indexed) with value 1.
#
# Let odd denote the number of odd indices in the binary representation of n
# (0-indexed) with value 1.
#
# Return an integer array answer where answer = [even, odd].
#
#
# Example 1:
#
#
# Input: n = 17
# Output: [2,0]
# Explanation: The binary representation of 17 is 10001.
# It contains 1 on the 0^th and 4^th indices.
# There are 2 even and 0 odd indices.
#
#
# Example 2:
#
#
# Input: n = 2
# Output: [0,1]
# Explanation: The binary representation of 2 is 10.
# It contains 1 on the 1^st index.
# There are 0 even and 1 odd indices.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:][::-1]
        answer = [0, 0]
        for i, bit in enumerate(binary):
            if bit == '1':
                if i % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
        return answer
# @lc code=end
