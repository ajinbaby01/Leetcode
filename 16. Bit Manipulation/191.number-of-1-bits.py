#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (69.92%)
# Likes:    6433
# Dislikes: 1331
# Total Accepted:    1.4M
# Total Submissions: 2M
# Testcase Example:  '11'
#
# Write a function that takes the binary representation of a positive integer
# and returns the number of set bits it has (also known as the Hamming
# weight).
#
#
# Example 1:
#
#
# Input: n = 11
#
# Output: 3
#
# Explanation:
#
# The input binary string 1011 has a total of three set bits.
#
#
# Example 2:
#
#
# Input: n = 128
#
# Output: 1
#
# Explanation:
#
# The input binary string 10000000 has a total of one set bit.
#
#
# Example 3:
#
#
# Input: n = 2147483645
#
# Output: 30
#
# Explanation:
#
# The input binary string 1111111111111111111111111111101 has a total of thirty
# set bits.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return self.convertToBinaryString(n)
        # return self.bitManipulation1(n)
        return self.bitManipulation2(n)

    def bitManipulation2(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)
            # n & (n - 1) removes the rightmost 1 bit
            # count the number of times 1 is deleted until n becomes 0
            count += 1
        return count

    def bitManipulation1(self, n: int) -> int:
        count = 0
        while n != 0:
            count = count + (n & 1)
            # (n & 1) = 1 if rightmost bit is 1 and 0 if rightmost bit is 0 (n is considered in binary)
            n = n >> 1
            # Right shift the number to remove the rightmost bit
        return count

    def convertToBinaryString(self, n: int) -> int:
        binary = bin(n)
        count = 0
        for digit in binary:
            if digit == "1":
                count += 1
        return count


# @lc code=end
