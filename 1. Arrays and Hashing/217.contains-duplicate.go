/*
 * @lc app=leetcode id=217 lang=golang
 *
 * [217] Contains Duplicate
 *
 * https://leetcode.com/problems/contains-duplicate/description/
 *
 * algorithms
 * Easy (61.22%)
 * Likes:    11813
 * Dislikes: 1288
 * Total Accepted:    3.9M
 * Total Submissions: 6.4M
 * Testcase Example:  '[1,2,3,1]'
 *
 * Given an integer array nums, return true if any value appears at least twice
 * in the array, and return false if every element is distinct.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3,1]
 * Output: true
 * Example 2:
 * Input: nums = [1,2,3,4]
 * Output: false
 * Example 3:
 * Input: nums = [1,1,1,3,3,4,3,2,4,2]
 * Output: true
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 *
 *
 */

// @lc code=start
func containsDuplicate(nums []int) bool {
	return constantSpace(nums)
	// return extraSpace(nums)
}

func constantSpace(nums []int) bool {
	sort.Ints(nums)
	for i := 0; i < len(nums) - 1; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}

func extraSpace(nums []int) bool {
	// Preallocate length to avoid resizing
	seen := make(map[int]bool, len(nums))
    for _, num := range nums {
		if _, ok := seen[num]; ok {
			// Return immediately if duplicate
			// instead of completing the loop
			return true
		}
		seen[num] = true
	}
	return false
}
// @lc code=end
