/*
 * @lc app=leetcode id=34 lang=golang
 *
 * [34] Find First and Last Position of Element in Sorted Array
 *
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (44.48%)
 * Likes:    22432
 * Dislikes: 605
 * Total Accepted:    2.9M
 * Total Submissions: 6.1M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * Given an array of integers nums sorted in non-decreasing order, find the
 * starting and ending position of a given target value.
 *
 * If target is not found in the array, return [-1, -1].
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 *
 * Example 1:
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 * Example 2:
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 * Example 3:
 * Input: nums = [], target = 0
 * Output: [-1,-1]
 *
 *
 * Constraints:
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * nums is a non-decreasing array.
 * -10^9 <= target <= 10^9
 *
 *
 */

// @lc code=start
package main

func searchRange(nums []int, target int) []int {
	res := []int{-1, -1}

	findBound := func(first bool) int {
		left, right := 0, len(nums)-1
		bound := -1
		for left <= right {
			mid := (left + right) / 2
			if nums[mid] == target {
				bound = mid
				if first {
					right = mid - 1
				} else {
					left = mid + 1
				}
			} else if nums[mid] < target {
				left = mid + 1
			} else if nums[mid] > target {
				right = mid - 1
			}
		}
		return bound
	}
	res[0] = findBound(true)
	res[1] = findBound(false)
	return res
}

// @lc code=end
