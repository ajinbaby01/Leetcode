#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (66.92%)
# Likes:    17160
# Dislikes: 504
# Total Accepted:    2.2M
# Total Submissions: 3.3M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashing is not needed. Check go code
        def hashstr(string):
            sorted_string = ''.join(sorted(string))
            # anagrams are the same when sorted
            return hash(sorted_string)
            # two anagrams will have the same hash

        # def group_strings(hashed_strings):
        #     grouped_strings = defaultdict(list)
        #     for string, h in hashed_strings:
        #             grouped_strings[h].append(string)
        #     return grouped_strings.values()

        # hashed_strings = [(string, hashstr(string)) for string in strs]

        # return group_strings(hashed_strings)
        # Time complexity = O(N * mlogm)
        # m = Length of longest string, N = No. of strings

        group = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)
        return group.values()
        # Time complexity = O(N * m)

# @lc code=end
