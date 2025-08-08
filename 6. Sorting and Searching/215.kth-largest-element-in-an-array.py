#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (67.14%)
# Likes:    16030
# Dislikes: 765
# Total Accepted:    2M
# Total Submissions: 2.9M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# Can you solve it without sorting?
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            heappush(minheap, -num)
        for _ in range(k):
            answer = -heappop(minheap)
        return answer

#Golang
# package main

# import (
# 	"container/heap"
# 	"fmt"
# )

# type MinHeap []int

# // Len implements heap.Interface.
# func (m MinHeap) Len() int {
# 	return len(m)
# }

# // Less implements heap.Interface.
# func (m MinHeap) Less(i int, j int) bool {
# 	return m[i] < m[j]
# }

# // Pop implements heap.Interface.
# func (m *MinHeap) Pop() any {
# 	old := *m
# 	n := len(old)
# 	x := old[n-1]
# 	*m = old[:n-1]
# 	return x
# }

# // Push implements heap.Interface.
# func (m *MinHeap) Push(x any) {
# 	*m = append(*m, x.(int))
# }

# // Swap implements heap.Interface.
# func (m MinHeap) Swap(i int, j int) {
# 	m[i], m[j] = m[j], m[i]
# }

# func kthLargest(nums []int, k int) int {
# 	h := &MinHeap{}
# 	heap.Init(h)
# 	for _, num := range nums {
# 		heap.Push(h, num)
# 		if h.Len() > k {
# 			heap.Pop(h)
# 		}
# 	}
# 	return (*h)[0]
# }

# func main() {
# 	arr := []int{3, 2, 1, 5, 6, 4}
# 	k := 2
# 	result := kthLargest(arr, k)
# 	fmt.Println("Kth largest element:", result)
# }

# @lc code=end
