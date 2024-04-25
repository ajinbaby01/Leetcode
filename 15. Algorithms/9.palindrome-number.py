#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (55.19%)
# Likes:    12324
# Dislikes: 2704
# Total Accepted:    4.5M
# Total Submissions: 8M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.mySolution(x)
        # return self.optimizedSolution(x)

    def optimizedSolution(self, x: int) -> bool:
        # Reverse given number into a variable until it's half-half.
        # Check the reversed part and the remaining part of original number.
        if (x < 0) or (x > 0 and x % 10 == 0):
            # If x is negative or if the last digit of x is 0
            return False

        reverse = 0
        while reverse < x:
            reverse = reverse * 10 + (x % 10)
            x = x // 10

        return True if (x == reverse or x == reverse // 10) else False

    def mySolution(self, x: int) -> bool:
        if (x < 0) or (x > 0 and x % 10 == 0):
            # If x is negative or if the last digit of x is 0
            return False

        palindrome = 0
        copy = x
        while x > 0:
            palindrome = palindrome * 10 + (x % 10)
            x = x // 10
        return palindrome == copy
# @lc code=end
