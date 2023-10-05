#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (43.28%)
# Likes:    15962
# Dislikes: 229
# Total Accepted:    751.3K
# Total Submissions: 1.7M
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Using an increasing monotonic stack

        # stack = []
        # max_area = 0

        # for index, height in enumerate(heights):
        #     i = index
        #     if not stack:
        #         stack.append((index, height))
        #         max_area = max(max_area, height)
        #     else:
        #         while stack and (stack[-1][1] > height):
        #             i, h = stack.pop()
        #             max_area = max(max_area, (index - i) * h)
        #         else:
        #             stack.append((i, height))
        #             max_area = max(max_area, height)

        # index += 1
        # while stack:
        #     i, h = stack.pop()
        #     max_area = max(max_area, (index - i) * h)

        # return max_area

        # Same logic and code flow as above but some optimizations to save time
        # and memory
        stack = []
        max_area = 0
        heights.append(0)
        # Can remove the lines 19-22 by appending 0 to heights, since 0
        # will be smallest height and will make sure the stack is emptied
        # (eg: if heights = [1,2,3,4,5])

        for index, height in enumerate(heights):
            i = index
            if stack and height == stack[-1][1]:
                continue
            # No need to store duplicates as the total area of duplicates can
            # be calculated from the index of the first occurence of the
            # duplicate
            while stack and (stack[-1][1] > height):
                i, h = stack.pop()
                max_area = max(max_area, (index - i) * h)
            # Line 15 (else) is redundant as no break or continue is used
            # Line 8-10 can be combined with the below code
            stack.append((i, height))
            max_area = max(max_area, height)

        return max_area
# @lc code=end
