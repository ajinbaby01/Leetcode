/*
 * @lc app=leetcode id=215 lang=golang
 *
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (66.79%)
 * Likes:    18245
 * Dislikes: 955
 * Total Accepted:    3.2M
 * Total Submissions: 4.7M
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Given an integer array nums and an integer k, return the k^th largest
 * element in the array.
 *
 * Note that it is the k^th largest element in the sorted order, not the k^th
 * distinct element.
 *
 * Can you solve it without sorting?
 *
 *
 * Example 1:
 * Input: nums = [3,2,1,5,6,4], k = 2
 * Output: 5
 * Example 2:
 * Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
 * Output: 4
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */

// @lc code=start
package main

import (
	"container/heap"
	"math/rand/v2"
)

type MinHeap []int

func (m MinHeap) Len() int {
	return len(m)
}

// Less defines who to take when you call pop
// Here the node with less value is popped
func (m MinHeap) Less(i int, j int) bool {
	return m[i] < m[j]
}

func (m *MinHeap) Pop() any {
	old := *m
	n := len(old)
	x := old[n-1]
	*m = old[:n-1]
	return x
}

func (m *MinHeap) Push(x any) {
	*m = append(*m, x.(int))
}

func (m MinHeap) Swap(i int, j int) {
	m[i], m[j] = m[j], m[i]
}

func findKthLargest(nums []int, k int) int {
	// return minHeap(nums, k)
	return quickSelectKthLargest(nums, k)
}

func quickSelectKthLargest(nums []int, k int) int {
	n := len(nums)
	k = n - k
	var quickSelect func(int, int) int
	quickSelect = func(l, r int) int {
		choice := l + rand.IntN(r-l+1)
		pivot := nums[choice]
		nums[r], nums[choice] = nums[choice], nums[r]

		p := l
		for i := l; i < r; i++ {
			if nums[i] < pivot {
				nums[p], nums[i] = nums[i], nums[p]
				p++
			}
		}
		nums[r], nums[p] = nums[p], nums[r]

		if p == k {
			return nums[p]
		} else if p > k {
			return quickSelect(l, p-1)
		} else {
			return quickSelect(p+1, r)
		}
	}
	return quickSelect(0, n-1)
}

// In min heap, root always have the least value
// When you pop after length exceeds k, the least value is popped.
// After processing n elements, the root contains the kth largest
func minHeap(nums []int, k int) int {
	h := &MinHeap{}
	heap.Init(h)
	for _, num := range nums {
		heap.Push(h, num)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return (*h)[0]
}

// @lc code=end
