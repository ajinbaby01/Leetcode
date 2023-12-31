#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (46.84%)
# Likes:    21401
# Dislikes: 737
# Total Accepted:    2.2M
# Total Submissions: 4.6M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlap(a, b):
            # Only need to check one case as we are sorting the intervals
            # return a[0] <= b[1] and b[0] <= a[1]
            return b[0] <= a[1]

        def merge_overlapping_intervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        # intervals.sort()
        res = []
        # for interval in intervals:
        for interval in sorted(intervals, key=lambda x: x[0]):
            if res and is_overlap(res[-1], interval):
                # merge = merge_overlapping_intervals(res[-1], interval)
                # # res.pop()
                # # res.append(merge)
                # res[-1][1] = merge[1]
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
# @lc code=end
