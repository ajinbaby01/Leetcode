/*
 * @lc app=leetcode id=2149 lang=golang
 *
 * [2149] Rearrange Array Elements by Sign
 *
 * https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
 *
 * algorithms
 * Medium (84.02%)
 * Likes:    3883
 * Dislikes: 220
 * Total Accepted:    696.1K
 * Total Submissions: 824.2K
 * Testcase Example:  '[3,1,-2,-5,2,-4]'
 *
 * You are given a 0-indexed integer array nums of even length consisting of an
 * equal number of positive and negative integers.
 *
 * You should return the array of nums such that the the array follows the
 * given conditions:
 *
 *
 * Every consecutive pair of integers have opposite signs.
 * For all integers with the same sign, the order in which they were present in
 * nums is preserved.
 * The rearranged array begins with a positive integer.
 *
 *
 * Return the modified array after rearranging the elements to satisfy the
 * aforementioned conditions.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,1,-2,-5,2,-4]
 * Output: [3,-2,1,-5,2,-4]
 * Explanation:
 * The positive integers in nums are [3,1,2]. The negative integers are
 * [-2,-5,-4].
 * The only possible way to rearrange them such that they satisfy all
 * conditions is [3,-2,1,-5,2,-4].
 * Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are
 * incorrect because they do not satisfy one or more conditions.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1,1]
 * Output: [1,-1]
 * Explanation:
 * 1 is the only positive integer and -1 the only negative integer in nums.
 * So nums is rearranged to [1,-1].
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 2 * 10^5
 * nums.length is even
 * 1 <= |nums[i]| <= 10^5
 * nums consists of equal number of positive and negative integers.
 *
 *
 *
 * It is not required to do the modifications in-place.
 */

// @lc code=start
func rearrangeArray(nums []int) []int {
	return separateNum(nums)
	// return optimal(nums)
}

func optimal(nums []int) []int {
	ans := make([]int, len(nums))
	posIdx, negIdx := 0, 1
	for _, num := range nums {
		if num > 0 {
			ans[posIdx] = num
			posIdx += 2
		} else if num < 0 {
			ans[negIdx] = num
			negIdx += 2
		}
	}
	return ans
}
// Time: O(n), Space: O(n)

func separateNum(nums []int) []int {
	var pos []int
	var neg []int
	for _, num := range nums {
		if num > 0 {
			pos = append(pos, num)
		} else {
			neg = append(neg, num)
		}
	}

	for i := 0; i < len(pos); i++ {
		nums[2*i] = pos[i]
		nums[2*i+1] = neg[i]
	}
	return nums
}
// Time: O(2n), Space: O(n)
// @lc code=end
