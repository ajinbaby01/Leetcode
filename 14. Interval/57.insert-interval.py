#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (39.72%)
# Likes:    9376
# Dislikes: 691
# Total Accepted:    908K
# Total Submissions: 2.3M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#

# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # return self.mySolution(intervals, newInterval)
        return self.neetcode(intervals, newInterval)

    def neetcode(self, intervals, newInterval):
        # Draw some intervals using straight lines.
        # There are three cases in which the newInterval can come:
        # 1 - newInterval's end is before current interval's start.
        # 2 - newInterval's start is after current interval's end.
        # 3 - If cases 1 and 2 are wrong, then newInterval and current interval overlaps.
        # In case 3, after merging newInterval and current interval,
        # the merged interval can overlap upcoming intervals. So repeat the cases.
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res

    def mySolution(self, intervals, newInterval):
        def is_overlap(a, b):
            # Only need to check one case as the intervals are sorted
            # return a[0] <= b[1] and b[0] <= a[1]
            return b[0] <= a[1]

        if not intervals:
            return [newInterval]

        # Using binary search to find the index to insert
        low, high = 0, len(intervals)
        while low < high:
            mid = (low + high) // 2
            if intervals[mid][0] < newInterval[0]:
                low = mid + 1
            else:
                high = mid

        res = []
        res = intervals[0:low]
        if res and is_overlap(res[-1], newInterval):
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        while low < len(intervals):
            if is_overlap(res[-1], intervals[low]):
                res[-1][1] = max(res[-1][1], intervals[low][1])
            else:
                res.append(intervals[low])
            low += 1
        return res
# @lc code=end
