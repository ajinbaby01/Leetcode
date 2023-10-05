#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.25%)
# Likes:    10603
# Dislikes: 331
# Total Accepted:    2.6M
# Total Submissions: 4.1M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pattern = [0]*26
        for c in s:
            pattern[ord(c) - ord('a')] += 1

        for c in t:
            pattern[ord(c) - ord('a')] -= 1

        for val in pattern:
            if val != 0:
                return False
        return True
# @lc code=end
