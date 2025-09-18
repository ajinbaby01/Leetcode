/*
 * @lc app=leetcode id=229 lang=golang
 *
 * [229] Majority Element II
 *
 * https://leetcode.com/problems/majority-element-ii/description/
 *
 * algorithms
 * Medium (51.71%)
 * Likes:    10662
 * Dislikes: 477
 * Total Accepted:    1.1M
 * Total Submissions: 2M
 * Testcase Example:  '[3,2,3]'
 *
 * Given an integer array of size n, find all elements that appear more than ⌊
 * n/3 ⌋ times.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,2,3]
 * Output: [3]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1]
 * Output: [1]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,2]
 * Output: [1,2]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 5 * 10^4
 * -10^9 <= nums[i] <= 10^9
 *
 *
 *
 * Follow up: Could you solve the problem in linear time and in O(1) space?
 *
 */

// @lc code=start
func majorityElement(nums []int) []int {
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
		if len(count) <= 2 {
			continue
		}

		for key := range count {
			count[key]--
			if count[key] == 0 {
				delete(count, key)
			}
		}
	}

	var res []int

	for key := range count {
		i := 0
		for _, num := range nums {
			if key == num {
				i++
			}
			if i > len(nums)/3 {
				res = append(res, num)
				break
			}
		}
	}
	return res
}

// @lc code=end
