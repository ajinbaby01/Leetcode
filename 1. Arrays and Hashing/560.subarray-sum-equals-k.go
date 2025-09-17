/*
 * @lc app=leetcode id=560 lang=golang
 *
 * [560] Subarray Sum Equals K
 *
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (43.72%)
 * Likes:    23937
 * Dislikes: 787
 * Total Accepted:    2M
 * Total Submissions: 4.3M
 * Testcase Example:  '[1,1,1]\n2'
 *
 * Given an array of integers nums and an integer k, return the total number of
 * subarrays whose sum equals to k.
 *
 * A subarray is a contiguous non-empty sequence of elements within an
 * array.
 *
 *
 * Example 1:
 * Input: nums = [1,1,1], k = 2
 * Output: 2
 * Example 2:
 * Input: nums = [1,2,3], k = 3
 * Output: 2
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -1000 <= nums[i] <= 1000
 * -10^7 <= k <= 10^7
 *
 *
 */

// @lc code=start
/*
Refer longest-subarray-with-given-sum-k first
*/
/*
1. What sumFrequencyMap represents
At any point, sumFrequencyMap[S] = number of indices i where prefix sum = S.
When you are at index j with currentSum, you check if (currentSum - k) exists.
If yes, then every earlier index i with prefix sum (currentSum - k) gives a unique subarray (i+1 … j) whose sum is exactly k.

2. Why it doesn’t double-count
Each subarray is defined by a unique pair (i, j).
You only count it when you reach the end index j.
You never revisit the same (i, j) pair later, because the loop always moves forward.
Even if currentSum repeats later:
That creates new (i, j') pairs with a different ending index j'.
Those are different subarrays, not repeats of the old one.
*/
func subarraySum(nums []int, k int) int {
	count := 0
	currentSum := 0 // This variable stores the prefix sum up to the current index

	// sumFrequencyMap stores: prefixSum -> frequency_of_this_sum_occurring
	// Initialize with sum 0 having occurred once. This handles cases where the
	// subarray itself starts from index 0 and sums to k.
	// For example, if nums = [3, 2, 1], k = 3.
	// When right = 0, currentSum = 3. We look for 3 - 3 = 0.
	// sumFrequencyMap[0] is 1, so we increment count by 1 (subarray [3]).
	sumFrequencyMap := make(map[int]int)
	sumFrequencyMap[0] = 1 // Key difference here: store frequency, and 0 sum occurs once initially

	for _, num := range nums { // Iterate through numbers directly
		currentSum += num // Update prefix sum

		// Check if (currentSum - k) has been seen before.
		// If it has, it means there are 'n' subarrays ending at the current position
		// that sum to k, where 'n' is the frequency of (currentSum - k) in the map.
		if freq, found := sumFrequencyMap[currentSum-k]; found {
			count += freq // Add the frequency of that previous sum to our total count
		}

		// Increment the frequency of the currentSum in the map.
		// If it's the first time, it will be initialized to 1.
		sumFrequencyMap[currentSum]++
	}

	return count
}
/*
Let's say:
P[1] = P[3] = 2, P[6] = 5 and k = 3
ie, sum from 0-1 = 2, 0-3 = 2, 0-6 = 5
2 prefix sum occurs at two indices 1 and 3
P[6] - P[1] = k
P[6] - P[3] = k
So there are two subarrays whose sum equals k
The frequency of prefix sum occurring is stored in the sumFrequencyMap
*/
// @lc code=end
