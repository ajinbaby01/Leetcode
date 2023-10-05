#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (58.49%)
# Likes:    17110
# Dislikes: 897
# Total Accepted:    1.7M
# Total Submissions: 3M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs",
            "8":"tuv", "9":"wxyz"
        }

        if not digits:
            return []

        # def recursion(index=0, path='', answer=[]):
        #     if index >= len(digits):
        #         answer.append(path)
        #         return
        #     string = dic[digits[index]]
        #     for char in string:
        #         recursion(index+1, path+char)
        #     return answer
        # return recursion(digits)
        answer = ['']
        for digit in digits:
            temp = list()
            for char in dic[digit]:
                for combination in answer:
                    temp.append(combination + char)
            answer = temp
        return answer

# @lc code=end
