/*
 * @lc app=leetcode id=540 lang=golang
 *
 * [540] Single Element in a Sorted Array
 *
 * https://leetcode.com/problems/single-element-in-a-sorted-array/description/
 *
 * algorithms
 * Medium (59.09%)
 * Likes:    12540
 * Dislikes: 232
 * Total Accepted:    1.1M
 * Total Submissions: 1.8M
 * Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
 *
 * You are given a sorted array consisting of only integers where every element
 * appears exactly twice, except for one element which appears exactly once.
 *
 * Return the single element that appears only once.
 *
 * Your solution must run in O(log n) time and O(1) space.
 *
 *
 * Example 1:
 * Input: nums = [1,1,2,3,3,4,4,8,8]
 * Output: 2
 * Example 2:
 * Input: nums = [3,3,7,7,10,11,11]
 * Output: 10
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^5
 *
 *
 */

// @lc code=start
func singleNonDuplicate(nums []int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		mid := (left + right) / 2

		if mid == 0 || mid == len(nums)-1 {
			return nums[mid]
		}

		if nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1] {
			return nums[mid]
		}

		if mid%2 == 1 {
			mid--
		}

		if nums[mid] == nums[mid+1] {
			left = mid + 2 // +2 to ignore the pair
		} else {
			right = mid - 1
		}
	}

	return nums[left]
}

// @lc code=end
