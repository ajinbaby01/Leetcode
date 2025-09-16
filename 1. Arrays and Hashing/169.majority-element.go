/*
 * @lc app=leetcode id=169 lang=golang
 *
 * [169] Majority Element
 *
 * https://leetcode.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (63.90%)
 * Likes:    18796
 * Dislikes: 603
 * Total Accepted:    2.8M
 * Total Submissions: 4.3M
 * Testcase Example:  '[3,2,3]'
 *
 * Given an array nums of size n, return the majority element.
 *
 * The majority element is the element that appears more than ⌊n / 2⌋ times.
 * You may assume that the majority element always exists in the array.
 *
 *
 * Example 1:
 * Input: nums = [3,2,3]
 * Output: 3
 * Example 2:
 * Input: nums = [2,2,1,1,1,2,2]
 * Output: 2
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 1 <= n <= 5 * 10^4
 * -10^9 <= nums[i] <= 10^9
 *
 *
 *
 * Follow-up: Could you solve the problem in linear time and in O(1) space?
 */

// @lc code=start
// Moore's Voting Algorithm:
// Count of majority element will always exceed the count of other items
func majorityElement(nums []int) int {
	count := 1
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		if res == nums[i] {
			count++
		} else {
			if count == 0 {
				res = nums[i]
				count = 1
			} else {
				count--
			}
		}
	}
	return res
}
// Time: O(n), Space: O(1)
// @lc code=end
