/*
 * @lc app=leetcode id=46 lang=golang
 *
 * [46] Permutations
 *
 * https://leetcode.com/problems/permutations/description/
 *
 * algorithms
 * Medium (78.54%)
 * Likes:    20316
 * Dislikes: 368
 * Total Accepted:    2.8M
 * Total Submissions: 3.4M
 * Testcase Example:  '[1,2,3]'
 *
 * Given an array nums of distinct integers, return all the possible
 * permutations. You can return the answer in any order.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3]
 * Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * Example 2:
 * Input: nums = [0,1]
 * Output: [[0,1],[1,0]]
 * Example 3:
 * Input: nums = [1]
 * Output: [[1]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * All the integers of nums are unique.
 *
 *
 */

// @lc code=start
func permute(nums []int) [][]int {
	var permutations [][]int
	var backtrack func(int)
	backtrack = func(slot int) {
		if slot == len(nums) {
			perm := make([]int, len(nums))
			copy(perm, nums)
			permutations = append(permutations, perm)
			return
		}
		for i := slot; i < len(nums); i++ {
			nums[slot], nums[i] = nums[i], nums[slot]
			backtrack(slot + 1)
			nums[slot], nums[i] = nums[i], nums[slot]
		}
	}
	backtrack(0)
	return permutations
}
// @lc code=end
