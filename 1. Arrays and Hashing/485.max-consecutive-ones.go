/*
 * @lc app=leetcode id=485 lang=golang
 *
 * [485] Max Consecutive Ones
 *
 * https://leetcode.com/problems/max-consecutive-ones/description/
 *
 * algorithms
 * Easy (59.35%)
 * Likes:    6422
 * Dislikes: 478
 * Total Accepted:    1.8M
 * Total Submissions: 2.9M
 * Testcase Example:  '[1,1,0,1,1,1]'
 *
 * Given a binary array nums, return the maximum number of consecutive 1's in
 * the array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,1,0,1,1,1]
 * Output: 3
 * Explanation: The first two digits or the last three digits are consecutive
 * 1s. The maximum number of consecutive 1s is 3.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,0,1,1,0,1]
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * nums[i] is either 0 or 1.
 *
 *
 */

// @lc code=start
func findMaxConsecutiveOnes(nums []int) int {
	count := 0
	maxCount := 0
	for _, num := range nums {
		if num == 1 {
			count++
		} else {
			count = 0
		}
		maxCount = max(maxCount, count)
	}
	return maxCount
}

// @lc code=end
