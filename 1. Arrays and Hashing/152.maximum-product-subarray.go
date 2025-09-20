/*
 * @lc app=leetcode id=152 lang=golang
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (34.95%)
 * Likes:    19829
 * Dislikes: 800
 * Total Accepted:    1.8M
 * Total Submissions: 5M
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find a subarray that has the largest product,
 * and return the product.
 *
 * The test cases are generated so that the answer will fit in a 32-bit
 * integer.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -10 <= nums[i] <= 10
 * The product of any subarray of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 *
 */

// @lc code=start
// Watch striver (don't read tuf article), not neetcode
func maxProduct(nums []int) int {
	// return findProductOfAllSubarray(nums)
	return prefixSuffixProduct(nums)
}

func prefixSuffixProduct(nums []int) int {
	maxProd := math.MinInt
	n := len(nums)
	prefixProduct, suffixProduct := 1, 1
	for i := 0; i < n; i++ {
		prefixProduct *= nums[i]
		suffixProduct *= nums[n-i-1]
		maxProd = max(maxProd, prefixProduct, suffixProduct)
		if nums[i] == 0 {
			prefixProduct = 1
		}
		if nums[n-i-1] == 0 {
			suffixProduct = 1
		}
	}
	return maxProd
}
// Time: O(n^2)

func findProductOfAllSubarray(nums []int) int {
	maxProd := math.MinInt
	for i := 0; i < len(nums); i++ {
		p := 1
		for j := i; j < len(nums); j++ {
			p = p * nums[j]
			maxProd = max(maxProd, p)
		}
	}

	return maxProd
}
// Time: O(n^2)
// @lc code=end
