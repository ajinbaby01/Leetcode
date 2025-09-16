/*
 * @lc app=leetcode id=75 lang=golang
 *
 * [75] Sort Colors
 *
 * https://leetcode.com/problems/sort-colors/description/
 *
 * algorithms
 * Medium (62.65%)
 * Likes:    20693
 * Dislikes: 735
 * Total Accepted:    3.2M
 * Total Submissions: 4.7M
 * Testcase Example:  '[2,0,2,1,1,0]'
 *
 * Given an array nums with n objects colored red, white, or blue, sort them
 * in-place so that objects of the same color are adjacent, with the colors in
 * the order red, white, and blue.
 *
 * We will use the integers 0, 1, and 2 to represent the color red, white, and
 * blue, respectively.
 *
 * You must solve this problem without using the library's sort function.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,0,2,1,1,0]
 * Output: [0,0,1,1,2,2]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,0,1]
 * Output: [0,1,2]
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 1 <= n <= 300
 * nums[i] is either 0, 1, or 2.
 *
 *
 *
 * Follow up: Could you come up with a one-pass algorithm using only constant
 * extra space?
 *
 */

// @lc code=start
package main

func sortColors(nums []int) {
	// bucketSort(nums)
	// twoPassWithoutCounting(nums)
	quickSortPartition(nums)
}

// Similar to twoPassWithoutCounting
// But here, in one pass, we use two pointers.
// Every element to the left of Left will be 0 and every element to the right of Right will be 2

/*
Elements to the left of left (i.e., nums[0] to nums[left-1]) are all 0s.
Elements to the right of right (i.e., nums[right+1] to nums[len(nums)-1]) are all 2s.
Elements between left and i-1 are all 1.

Case 1: left < i This means there were elements between left and i. Then the statement "Elements between left and i-1 are all 1" applies, and nums[left] must have been 1. The swap places this 1 at nums[i], which is fine, as we'd expect. Thus we can increment i.

Case 2: left == i This means that no elements were in between left and i-1.
nums[i] is still swapped with nums[left] (nums[i] is equal to nums[left]), then increment i and left.

When nums[i] == 2, you swap with nums[right]. However, you have no idea what the value at nums[right] was before the swap. It could be a 0, a 1, or a 2. That's why you must re-examine nums[i] in the next iteration when nums[i] == 2.
*/
func quickSortPartition(nums []int) {
	left, right, i := 0, len(nums) - 1, 0
	for i <= right {
		if nums[i] == 0 {
			nums[left], nums[i] = nums[i], nums[left]
			left++
			i++
		} else if nums[i] == 2 {
			nums[right], nums[i] = nums[i], nums[right]
			right--
		} else {
			i++
		}
	}
}

func twoPassWithoutCounting(nums []int) {
	i, j:= 0, 0
	partition := func(i, j, k int) int {
		for j < len(nums) {
			if nums[j] == k {
				nums[i], nums[j] = nums[j], nums[i]
				i++
				j++
			} else {
				j++
			}
		}
		return i
	}
	i = partition(i, j, 0)
	j = i
	partition(i, j, 1)
}

func bucketSort(nums []int) {
	var count [3]int
	for _, num := range nums {
		if num == 0 {
			count[0]++
		} else if num == 1 {
			count[1]++
		} else {
			count[2]++
		}
	}
	i := 0
	k := 0
	for k <= 2 {
		for range count[k] {
			nums[i] = k
			i++
		}
		k++
	}
}
// @lc code=end
