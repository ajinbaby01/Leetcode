#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (41.31%)
# Likes:    5635
# Dislikes: 389
# Total Accepted:    2.4M
# Total Submissions: 5.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin Karp Algorithm and KMP Algorithm can also be used

        # return self.bruteForceSolution(haystack, needle)
        return self.slicingBruteForce(haystack, needle)

    def slicingBruteForce(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    # Time: O(n * m), Space: O(1)

    def bruteForceSolution(self, haystack: str, needle: str) -> int:
        i = 0
        # Ensure that there are enough characters left in the haystack for the needle to fit.
        # while i != (len(haystack) - len(needle)) fails because haystack can be smaller than needle
        while i <= (len(haystack) - len(needle)):
            j = 0
            k = i
            while (k != len(haystack)) and (j != len(needle)) and (haystack[k] == needle[j]):
                k += 1
                j += 1
            if j == len(needle):
                return i
            i += 1
        return -1
    # Time: O(n * m), Space: O(1)

# @lc code=end
