/*
 * @lc app=leetcode id=410 lang=golang
 *
 * [410] Split Array Largest Sum
 *
 * https://leetcode.com/problems/split-array-largest-sum/description/
 *
 * algorithms
 * Hard (55.52%)
 * Likes:    10939
 * Dislikes: 262
 * Total Accepted:    549.5K
 * Total Submissions: 929.4K
 * Testcase Example:  '[7,2,5,10,8]\n2'
 *
 * Given an integer array nums and an integer k, split nums into k non-empty
 * subarrays such that the largest sum of any subarray is minimized.
 *
 * Return the minimized largest sum of the split.
 *
 * A subarray is a contiguous part of the array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [7,2,5,10,8], k = 2
 * Output: 18
 * Explanation: There are four ways to split nums into two subarrays.
 * The best way is to split it into [7,2,5] and [10,8], where the largest sum
 * among the two subarrays is only 18.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,4,5], k = 2
 * Output: 9
 * Explanation: There are four ways to split nums into two subarrays.
 * The best way is to split it into [1,2,3] and [4,5], where the largest sum
 * among the two subarrays is only 9.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 1000
 * 0 <= nums[i] <= 10^6
 * 1 <= k <= min(50, nums.length)
 *
 *
 */

// @lc code=start
package main

import "slices"

func splitArray(nums []int, k int) int {
	left, right := slices.Max(nums), sumSlice(nums)
	if k == 1 {
		return right
	}
	if k == len(nums) {
		return left
	}

	for left <= right {
		mid := left + (right-left)/2
		if countSubArrays(nums, mid) > k {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

func countSubArrays(nums []int, mid int) int {
	subArray := 1
	sum := 0
	for _, num := range nums {
		if sum + num > mid {
			sum = 0
			subArray++
		}
		sum += num
	}
	return subArray
}

func sumSlice(nums []int) int {
	sum := 0
	for _, w := range nums {
		sum += w
	}
	return sum
}

// @lc code=end
