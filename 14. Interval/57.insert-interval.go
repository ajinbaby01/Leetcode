/*
 * @lc app=leetcode id=57 lang=golang
 *
 * [57] Insert Interval
 *
 * https://leetcode.com/problems/insert-interval/description/
 *
 * algorithms
 * Medium (39.72%)
 * Likes:    9376
 * Dislikes: 691
 * Total Accepted:    908K
 * Total Submissions: 2.3M
 * Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
 *
 * You are given an array of non-overlapping intervals intervals where
 * intervals[i] = [starti, endi] represent the start and the end of the i^th
 * interval and intervals is sorted in ascending order by starti. You are also
 * given an interval newInterval = [start, end] that represents the start and
 * end of another interval.
 *
 * Insert newInterval into intervals such that intervals is still sorted in
 * ascending order by starti and intervals still does not have any overlapping
 * intervals (merge overlapping intervals if necessary).
 *
 * Return intervals after the insertion.
 *
 *
 * Example 1:
 *
 *
 * Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
 * Output: [[1,5],[6,9]]
 *
 *
 * Example 2:
 *
 *
 * Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * Output: [[1,2],[3,10],[12,16]]
 * Explanation: Because the new interval [4,8] overlaps with
 * [3,5],[6,7],[8,10].
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^5
 * intervals is sorted by starti in ascending order.
 * newInterval.length == 2
 * 0 <= start <= end <= 10^5
 *
 *
 */

// @lc code=start
func insert(intervals [][]int, newInterval []int) [][]int {
	if len(intervals) == 0 {
		return [][]int{newInterval}
	}
	var insertedIntervals [][]int
	i := 0
	// Find the point where newInterval should be inserted
	for ; i < len(intervals) && intervals[i][1] < newInterval[0]; i++ {
		insertedIntervals = append(insertedIntervals, intervals[i])
	}

	// Merge all intervals overlapping with newInterval (There can be 0 overlaps also)
	mergedInterval := newInterval
	for i < len(intervals) && isOverlapping(mergedInterval, intervals[i]) {
		mergedInterval = mergeTwoIntervals(mergedInterval, intervals[i])
		i++
	}
	// Insert the merged interval to result (in case of 0 overlap, mergedInterval will be newInterval)
	insertedIntervals = append(insertedIntervals, mergedInterval)

	// Whatever intervals remain after the inserting the merged interval/inserting new interval, can be inserted as is
	return append(insertedIntervals, intervals[i:]...)
}

func isOverlapping(a, b []int) bool {
	return a[1] >= b[0]
}

func mergeTwoIntervals(a, b []int) []int {
	return []int{min(a[0], b[0]), max(a[1], b[1])}
}

// @lc code=end
