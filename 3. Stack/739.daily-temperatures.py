#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.93%)
# Likes:    11723
# Dislikes: 256
# Total Accepted:    708.4K
# Total Submissions: 1.1M
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Using monotonic decreasing stack. https://www.youtube.com/watch?v=Dq_ObZwTY_Q
        # stack = []
        # output = [0]*len(temperatures)

        # for i in range(len(temperatures) - 1, -1, -1):
        #     while stack and temperatures[i] >= temperatures[stack[-1]]:
        #         stack.pop()
        #     if stack:
        #         output[i] = stack[-1] - i
        #     stack.append(i)
        # return output

        # Neetcode solution. Using monotonic decreasing stack
        output = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)
        return output
# @lc code=end
