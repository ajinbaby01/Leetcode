/*
 * @lc app=leetcode id=189 lang=golang
 *
 * [189] Rotate Array
 *
 * https://leetcode.com/problems/rotate-array/description/
 *
 * algorithms
 * Medium (40.76%)
 * Likes:    20050
 * Dislikes: 2136
 * Total Accepted:    3.4M
 * Total Submissions: 7.8M
 * Testcase Example:  '[1,2,3,4,5,6,7]\n3'
 *
 * Given an integer array nums, rotate the array to the right by k steps, where
 * k is non-negative.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 * Explanation:
 * rotate 1 steps to the right: [7,1,2,3,4,5,6]
 * rotate 2 steps to the right: [6,7,1,2,3,4,5]
 * rotate 3 steps to the right: [5,6,7,1,2,3,4]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1,-100,3,99], k = 2
 * Output: [3,99,-1,-100]
 * Explanation:
 * rotate 1 steps to the right: [99,-1,-100,3]
 * rotate 2 steps to the right: [3,99,-1,-100]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -2^31 <= nums[i] <= 2^31 - 1
 * 0 <= k <= 10^5
 *
 *
 *
 * Follow up:
 *
 *
 * Try to come up with as many solutions as you can. There are at least three
 * different ways to solve this problem.
 * Could you do it in-place with O(1) extra space?
 *
 *
 */

// @lc code=start
// Brute force approach is to copy last k elements to an array
// and copy first n-k elements to the array
// In place solution is to reverse first n-k and last k, then reverse the whole thing
package main

func rotate(nums []int, k int) {
	// reversing(nums, k)
	jugglingAlgorithm(nums, k)
}

// Relies on the gcd(k, n)
func jugglingAlgorithm(nums []int, k int) {
	n := len(nums)
	k = k % n
	count := 0

	// Outer loop runs gcd(k, n) times
	for start := 0; count < n; start++ {
		current := start

		// prev stores the element to be replaced
		// Initialized to nums[start] for easy swapping in inner loop.
		// It is not the actual element that was replaced
		// That element is set in the inner loop
		prev := nums[start]

		// Inner loop represents one cycle. It will be executed gcd(k, n) times
		// Hence there will be gcd(k, n) cycles
		for {
			// next is the position where the element at current should be placed
			next := (current + k) % n

			// Here prev is set to the element that was replaced
			nums[next], prev = prev, nums[next]
			current = next
			count++

			// If we again reached the start of a cycle
			// we break out and start a new cycle staring from start + 1
			if start == current {
				break
			}
		}
	}
}

func reversing(nums []int, k int) {
	n := len(nums)
	k = k % n
	// slices.Reverse(nums[:n-k])
	// slices.Reverse(nums[n-k:])
	// slices.Reverse(nums)
	i, j := 0, n-k-1
	reverse(nums, i, j)
	i, j = n-k, n-1
	reverse(nums, i, j)
	i, j = 0, n-1
	reverse(nums, i, j)
}

func reverse(nums []int, i, j int) {
	for i < j {
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
}

// @lc code=end
