#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (60.07%)
# Likes:    8271
# Dislikes: 266
# Total Accepted:    1.5M
# Total Submissions: 2.4M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        st = set()
        dt = dict()
        for idx, char in enumerate(s):
            if char not in st:
                st.add(char)
                dt[char] = idx
            elif char in dt:
                dt.pop(char)

        # In python 3.7+, the dictionary is an ordered dict by default
        # So, the first idx in dt.values() will be the answer
        # iter(dt.values()) gives an iterator
        # Calling next once on it gives the first value
        # If dt is empty return -1
        return next(iter(dt.values()), -1)
        # return next(iter(dt.values())) if dt else -1
        # return min(dt.values()) if dt else -1
# @lc code=end
