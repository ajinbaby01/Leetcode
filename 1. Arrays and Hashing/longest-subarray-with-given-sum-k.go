// Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
// Example 1:
// Input Format: N = 3, k = 5, array[] = {2,3,5}
// Result: 2
// Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

// Example 2:
// Input Format: N = 5, k = 10, array[] = {1,3,5,2,9}
// Result: 3
// Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

package main

import (
	"fmt"
	"reflect"
)

// Two Pointer
func longestSubarrayPositive(nums []int, k int) []int {
	if len(nums) == 0 {
		return []int{}
	}

	left := 0       // Left pointer of the sliding window
	currentSum := 0 // Sum of elements in nums[left...right]
	maxLength := 0  // Stores the maximum length found so far
	start := 0      // Starting index of longest subarray

	for right := range nums {
		currentSum += nums[right] // Expand window to the right

		// Shrink window from the left if currentSum exceeds k
		// This loop runs as long as the sum is too large AND the window is valid (left <= right)
		for currentSum > k && left <= right {
			currentSum -= nums[left]
			left++
		}

		// If currentSum is exactly k, update maxLength
		// This check happens after shrinking, so currentSum is either == k or < k
		if currentSum == k {
			if right-left+1 > maxLength {
				start = left
				maxLength = right - left + 1
			}
		}
		// If currentSum < k, the window is valid but doesn't sum to k.
		// We continue expanding to the right.
	}

	return nums[start : start+maxLength]
}

// Prefix Sums: We iterate through the array, maintaining a currentSum (which is essentially the prefix sum up to the current index).
// Hash Map: We store (prefixSum, index) pairs in a hash map. The key is the prefix sum, and the value is the earliest index where that prefix sum was encountered.
// Target Calculation: If we are looking for a subarray nums[i...j] that sums to k, this means:
// prefixSum[j] - prefixSum[i-1] == k
// Rearranging this, we get:
// prefixSum[i-1] == prefixSum[j] - k
// So, for each currentPrefixSum (prefixSum[j]), we check if currentPrefixSum - k exists as a key in our hash map. If it does, it means we found an earlier prefixSum[i-1] that satisfies the condition.
// Longest Subarray: To find the longest subarray, when we store a prefixSum in the map, we only store it if it's the first time we've seen that sum. If we encounter the same prefix sum again, we keep the earlier index, as current_index - earlier_index will yield a longer subarray length.
func longestSubarrayPositiveNegative(nums []int, k int) []int {
	maxLength := 0
	start := 0
	currentSum := 0 // This variable stores the prefix sum up to the current index

	// sumToIndexMap stores: prefixSum -> earliest_index_where_this_sum_occurred
	// Initialize with sum 0 at index -1. This handles cases where the
	// subarray itself starts from index 0 and sums to k. (subarray starts from 0 to right index)
	// For example, if nums = [3, 2, 1], k = 3.
	// When right = 0, currentSum = 3. We look for 3 - 3 = 0.
	// If 0 is found at index -1, then length = 0 - (-1) = 1 (subarray [3]).
	sumToIndexMap := make(map[int]int)
	sumToIndexMap[0] = -1

	for right := 0; right < len(nums); right++ {
		currentSum += nums[right] // Update prefix sum

		// Check if (currentSum - k) has been seen before.
		// If it has, it means the subarray from (index_of_currentSum-k + 1) to 'right'
		// sums exactly to k.
		if prevIndex, found := sumToIndexMap[currentSum-k]; found {
			if maxLength < right-prevIndex {
				maxLength = right - prevIndex
				start = prevIndex + 1
			}
		}

		// Store the currentSum and its index, but ONLY if it's the first time
		// we've seen this sum. This is crucial for finding the *longest* subarray.
		// If we've seen this sum before, the existing index is earlier,
		// and (right - earlier_index) would produce a longer result.
		if _, found := sumToIndexMap[currentSum]; !found {
			sumToIndexMap[currentSum] = right
		}
	}

	return nums[start : start+maxLength]
}

func main() {
	positiveTestCases := []struct {
		Nums []int
		k    int
		ans  []int
	}{
		{Nums: []int{1, 1, 1, 1, 5}, k: 5, ans: []int{5}},
		{Nums: []int{2, 2, 2, 2}, k: 8, ans: []int{2, 2, 2, 2}},
		{Nums: []int{1, 2, 3}, k: 7, ans: []int{}},
		{Nums: []int{5, 1, 2, 3}, k: 5, ans: []int{2, 3}},
		{Nums: []int{}, k: 0, ans: []int{}},
		{Nums: []int{0, 0, 0, 0}, k: 0, ans: []int{0, 0, 0, 0}},
		{Nums: []int{1, 2, 3, 4, 5}, k: 100, ans: []int{}},
	}

	allTestCases := []struct {
		Nums []int
		k    int
		ans  []int
	}{
		{Nums: []int{1, 1, 1, 1, 5}, k: 5, ans: []int{5}},
		{Nums: []int{2, 2, 2, 2}, k: 8, ans: []int{2, 2, 2, 2}},
		{Nums: []int{1, 2, 3}, k: 7, ans: []int{}},
		{Nums: []int{5, 1, 2, 3}, k: 5, ans: []int{2, 3}},
		{Nums: []int{}, k: 0, ans: []int{}},
		{Nums: []int{0, 0, 0, 0}, k: 0, ans: []int{0, 0, 0, 0}},
		{Nums: []int{1, 2, 3, 4, 5}, k: 100, ans: []int{}},
		{Nums: []int{1, -1, 2, -2, 3, -3, 4}, k: 4, ans: []int{1, -1, 2, -2, 3, -3, 4}},
		{Nums: []int{2, -1, 2, 3}, k: 4, ans: []int{-1, 2, 3}},
		{Nums: []int{1, 2, -1, 2, -1, 2}, k: 3, ans: []int{1, 2, -1, 2, -1}},
		{Nums: []int{10, -10, 10, -10, 10}, k: 0, ans: []int{10, -10, 10, -10}},
		{Nums: []int{9, -3, 3, -1, 6, -5}, k: 0, ans: []int{-3, 3, -1, 6, -5}},
	}
	for _, t := range positiveTestCases {
		ans := longestSubarrayPositive(t.Nums, t.k)
		if !reflect.DeepEqual(t.ans, ans) {
			fmt.Println(t, ans)
			panic("failed")
		}
	}
	for _, t := range allTestCases {
		ans := longestSubarrayPositiveNegative(t.Nums, t.k)
		if !reflect.DeepEqual(t.ans, ans) {
			fmt.Println(t, ans)
			panic("failed")
		}
	}
	fmt.Println("Passed")
}
