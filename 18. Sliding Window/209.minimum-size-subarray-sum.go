/*
 * @lc app=leetcode id=209 lang=golang
 *
 * [209] Minimum Size Subarray Sum
 *
 * https://leetcode.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (47.25%)
 * Likes:    13721
 * Dislikes: 513
 * Total Accepted:    1.6M
 * Total Submissions: 3.1M
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * Given an array of positive integers nums and a positive integer target,
 * return the minimal length of a subarray whose sum is greater than or equal
 * to target. If there is no such subarray, return 0 instead.
 *
 *
 * Example 1:
 *
 *
 * Input: target = 7, nums = [2,3,1,2,4,3]
 * Output: 2
 * Explanation: The subarray [4,3] has the minimal length under the problem
 * constraint.
 *
 *
 * Example 2:
 *
 *
 * Input: target = 4, nums = [1,4,4]
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: target = 11, nums = [1,1,1,1,1,1,1,1]
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= target <= 10^9
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^4
 *
 *
 *
 * Follow up: If you have figured out the O(n) solution, try coding another
 * solution of which the time complexity is O(n log(n)).
 */

// @lc code=start
func minSubArrayLen(target int, nums []int) int {
	// return bruteForce(target, nums)
	return slidingWindow(target, nums)
}

func slidingWindow(target int, nums []int) int {
	left, currSum := 0, 0
	minLen := math.MaxInt

	for right, val := range nums {
		currSum += val
		// always expand right until the sum meets/exceeds the target, then shrink from the left.
		for currSum >= target {
			minLen = min(minLen, right-left+1)
			currSum -= nums[left]
			left++
		}
	}

	if minLen == math.MaxInt {
		return 0
	}
	return minLen
}
// Time: O(n)

func bruteForce(target int, nums []int) int {
	minLen := math.MaxInt

	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum >= target {
				minLen = min(minLen, j-i+1)
			}
		}
	}

	if minLen == math.MaxInt {
		return 0
	}
	return minLen
}
// Time: O(n^2)
// @lc code=end
