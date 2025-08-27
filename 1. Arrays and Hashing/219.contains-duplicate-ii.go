/*
 * @lc app=leetcode id=219 lang=golang
 *
 * [219] Contains Duplicate II
 *
 * https://leetcode.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (44.20%)
 * Likes:    6019
 * Dislikes: 3065
 * Total Accepted:    928.1K
 * Total Submissions: 2.1M
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * Given an integer array nums and an integer k, return true if there are two
 * distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
 * - j) <= k.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,1], k = 3
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,0,1,1], k = 1
 * Output: true
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,2,3,1,2,3], k = 2
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 0 <= k <= 10^5
 *
 *
 */

// @lc code=start
func containsNearbyDuplicate(nums []int, k int) bool {
	seen := make(map[int]int, len(nums))
    for i, num := range nums {
		if j, ok := seen[num]; ok {
			if math.Abs(float64(i - j)) <= float64(k) {
				return true
			}
		}
		// In case of duplicates, we override the index
		// so that when we see the next duplicate the difference between
		// the indices is the smallest
		seen[num] = i
	}
	return false
}
// @lc code=end
