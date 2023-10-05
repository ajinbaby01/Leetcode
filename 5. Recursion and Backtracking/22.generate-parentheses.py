#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.34%)
# Likes:    19631
# Dislikes: 799
# Total Accepted:    1.5M
# Total Submissions: 2.1M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtracking(openN, closeN + 1)
                stack.pop()

        backtracking(0, 0)
        return res
# @lc code=end
