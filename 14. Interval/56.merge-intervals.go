/*
 * @lc app=leetcode id=56 lang=golang
 *
 * [56] Merge Intervals
 *
 * https://leetcode.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (46.84%)
 * Likes:    21401
 * Dislikes: 737
 * Total Accepted:    2.2M
 * Total Submissions: 4.6M
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * Given an array of intervals where intervals[i] = [starti, endi], merge all
 * overlapping intervals, and return an array of the non-overlapping intervals
 * that cover all the intervals in the input.
 *
 *
 * Example 1:
 *
 *
 * Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
 * [1,6].
 *
 *
 * Example 2:
 *
 *
 * Input: intervals = [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^4
 *
 *
 */

// @lc code=start
func merge(intervals [][]int) [][]int {
	// Sort intervals by each interval's starting value
	slices.SortFunc(intervals, func(a, b []int) int {
		return a[0] - b[0]
	})

	/*
	This makes a shallow copy.
	Changing the first element of mergedIntervals will change intervals.
	Since we are not modifying anything here, it's fine.
	To deep copy:
		first := append([]int(nil), intervals[0]...)
		mergedIntervals := [][]int{first}
	*/
	mergedIntervals := [][]int{intervals[0]}

	for i := 1; i < len(intervals); i++ {
		lastInterval := mergedIntervals[len(mergedIntervals)-1]
		if isOverlapping(lastInterval, intervals[i]) {
			mergedInterval := mergeTwoIntervals(lastInterval, intervals[i])
			mergedIntervals[len(mergedIntervals)-1] = mergedInterval
		} else {
			mergedIntervals = append(mergedIntervals, intervals[i])
		}
	}
	return mergedIntervals
}

/*
Since the intervals are sorted, a[0] <= b[0]
It is given that 0 <= starti <= endi.
ie, b[0] <= b[1]
Therefore, a[0] <= b[1].
That's why this check is not included
*/
func isOverlapping(a, b []int) bool {
	return a[1] >= b[0]
}

func mergeTwoIntervals(a, b []int) []int {
	return []int{min(a[0], b[0]), max(a[1], b[1])}
}
// Time: O(N*logN) + O(N)
// Space: O(N)
// @lc code=end
