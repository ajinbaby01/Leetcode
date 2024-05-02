#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (77.82%)
# Likes:    10969
# Dislikes: 524
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^5
#
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
#
#
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Input: n = 5
        # Output: [0,1,1,2,1,2]
        # Explanation:
        # 0 --> 0
        # 1 --> 1
        # 2 --> 10
        # 3 --> 11
        # 4 --> 100
        # 5 --> 101
        # return self.builtin(n)
        # return self.nonBuiltin(n)
        return self.linearTime(n)

    def linearTime(self, n: int) -> List[int]:
        # Any number and its double will have the same number of 1’s.
        # Likewise, doubling a number and adding one will increase the count by exactly 1.

        # countBits(N) = countBits(2N)
        # countBits(N)+1 = countBits(2N+1)

        # Any number will have the same bit count as half that number, with an extra one if it’s an odd number
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + i % 2
        return ans


    def nonBuiltin(self, n: int) -> List[int]:
        # Brian Kernighan’s algorithm
        ans = []
        for i in range(n + 1):
            count = 0
            while i != 0:
                i = i & (i - 1)
                count += 1
            ans.append(count)
        return ans
    # Time: O(nlogn)

    def builtin(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1): # O(n)
            binary = bin(i) # O(logi)
            count = 0
            for digit in binary: # O(logi)
                if digit == '1':
                    count += 1
            ans[i] = count
        return ans
    # The number of iterations of the inner loop in the entire outer loop can be approximated as the sum of logarithms from 1 to n.
    # log(1) + log(2) + ... + log(n) = log(1 * 2 * ... * n) = log(n!)
    # Using Stirling's approximation, n! ≈ sqrt(2πn) * (n/e)^n.
    # log(n!) ≈ log(sqrt(2πn) * (n/e)^n) ≈ n * log(n) - n
    # Time: O(n * log(n) - n) = O(nlogn)
# @lc code=end
