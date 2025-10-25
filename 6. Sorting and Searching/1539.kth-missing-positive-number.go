/*
 * @lc app=leetcode id=1539 lang=golang
 *
 * [1539] Kth Missing Positive Number
 *
 * https://leetcode.com/problems/kth-missing-positive-number/description/
 *
 * algorithms
 * Easy (60.07%)
 * Likes:    7663
 * Dislikes: 551
 * Total Accepted:    747.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '[2,3,4,7,11]\n5'
 *
 * Given an array arr of positive integers sorted in a strictly increasing
 * order, and an integer k.
 *
 * Return the k^th positive integer that is missing from this array.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [2,3,4,7,11], k = 5
 * Output: 9
 * Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
 * 5^th missing positive integer is 9.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [1,2,3,4], k = 2
 * Output: 6
 * Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
 * positive integer is 6.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 1000
 * 1 <= arr[i] <= 1000
 * 1 <= k <= 1000
 * arr[i] < arr[j] for 1 <= i < j <= arr.length
 *
 *
 *
 * Follow up:
 *
 * Could you solve this problem in less than O(n) complexity?
 *
 */

// @lc code=start
package main

func findKthPositive(arr []int, k int) int {
	return linearSearch(arr, k)
	// return binarySearch(arr, k)
}

func binarySearch(arr []int, k int) int {
	left, right := 0, len(arr)-1
	for left <= right {
		mid := left + (right-left)/2
		missingCountAtIndexMid := arr[mid] - (mid + 1) // correct number at mid is mid + 1 if no number is missing
		if missingCountAtIndexMid < k {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left + k
}

func linearSearch(arr []int, k int) int {
	for _, num := range arr {
		if num <= k {
			k++
		} else {
			break
		}
	}
	return k
}

// Time: O(n), Space: O(1)
// @lc code=end
