#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.53%)
# Likes:    7675
# Dislikes: 390
# Total Accepted:    631.8K
# Total Submissions: 1.6M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
#
# Example 1:
#
#
# Input: s = "aba"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                one = s[l:r]
                two = s[l+1:r+1]
                return one == one[::-1] or two == two[::-1]
        return True
# @lc code=end
