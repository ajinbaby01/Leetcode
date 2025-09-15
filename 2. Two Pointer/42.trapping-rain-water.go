/*
 * @lc app=leetcode id=42 lang=golang
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (62.20%)
 * Likes:    34960
 * Dislikes: 636
 * Total Accepted:    3.1M
 * Total Submissions: 4.7M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 *
 *
 * Example 1:
 *
 *
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 *
 *
 * Example 2:
 *
 *
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 *
 *
 *
 * Constraints:
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

// @lc code=start
package main

func trap(height []int) int {
	// return bruteForce(height)
	// return storeTallestHeights(height)
	return optimalSolution(height)
}

func optimalSolution(height []int) int {
	rain := 0
	n := len(height)
	left, right := 0, n - 1
	leftMax, rightMax := 0, 0
	for left <= right {
		if height[left] <= height[right] {
			leftMax = max(leftMax, height[left])
			rain += leftMax - height[left]
			left++
		} else {
			rightMax = max(rightMax, height[right])
			rain += rightMax - height[right]
			right--
		}
	}
	return rain
}
// Time: O(n), Space: O(1)

// Instead of calculating tallest to the left and right of i at each turn
// we will calculate and store the tallest using two arrays in one loop
func storeTallestHeights(height []int) int {
	rain := 0
	n := len(height)
	leftMax := make([]int, n)
	rightMax := make([]int, n)
	tallestLeft, tallestRight := 0, 0

	for i := range n {
		// leftMax[i] stores the maximum height to the left of i
		leftMax[i] = max(tallestLeft, height[i])
		tallestLeft = leftMax[i]

		// rightMax[i] stores the maximum height to the right of i
		rightMax[n-i-1] = max(tallestRight, height[n-i-1])
		tallestRight = rightMax[n-i-1]
	}

	for i := range n {
		waterAtIndexI := min(leftMax[i], rightMax[i]) - height[i]
		rain += waterAtIndexI
	}

	return rain
}
// Time: O(n), Space: O(n)

// Water at index i = min(tallest to the left of i, tallest to the right of i) - height at i
// Rain = sum of water at index 0 to len(height) - 1
func bruteForce(height []int) int {
	rain := 0
	n := len(height)
	for i := range n {
		leftMax, rightMax := height[i], height[i]
		for j := 0; j < i; j++ {
			// tallest to the left of i
			leftMax = max(leftMax, height[j])
		}

		for j := i + 1; j < len(height); j++ {
			// tallest to the right of i
			rightMax = max(rightMax, height[j])
		}

		waterAtIndexI := (min(leftMax, rightMax) - height[i])
		rain += waterAtIndexI
	}
	return rain
}
// Time: O(n^2), Space: O(1)
// @lc code=end
